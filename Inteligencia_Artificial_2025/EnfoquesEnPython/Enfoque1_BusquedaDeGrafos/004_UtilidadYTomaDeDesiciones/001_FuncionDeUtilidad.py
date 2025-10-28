# ================================
# Utilidad y toma de decisiones en grafos (sin librerías)
# ================================

# Grafo estocástico: en cada estado (nodo) hay acciones; cada acción tiene
# una lista de resultados (siguiente_estado, probabilidad, recompensa_inmediata).
grafo = {
    'A': {
        'safe':  [('B', 1.0,  +5)],
        'risky': [('C', 0.6, +12), ('D', 0.4, -8)]
    },
    'B': {},   # terminal
    'C': {},   # terminal
    'D': {}    # terminal
}

#    Estado A
#    /     \
# safe     risky
#  |         \
#  v          \
#   B (terminal, +10)
#             ↙      ↘
#         0.6 a C    0.4 a D
#        ( +12 )     ( -8 )
#  C (terminal, 0)   D (terminal, 0)




# Recompensa final al llegar a un nodo terminal (si no está, se asume 0).
recompensa_terminal = {
    'B': 10,
    'C': 0,
    'D': 0
}

# ------------------------------
# Funciones de utilidad (elige una)
# ------------------------------
def utilidad_neutral(x):
    return x

def utilidad_aversa(x):
    # Aversión al riesgo (suaviza ganancias/perdidas)
    # Nota: maneja negativos de manera continua
    return (x + 100.0)**0.5 - 10.0  # shift para evitar sqrt de negativo

def utilidad_buscadora(x):
    # Búsqueda de riesgo (exagera magnitudes)
    return x * abs(x) / 20.0  # cuadrática con escala

# Elige la utilidad a usar
U = utilidad_neutral   # cambia a utilidad_aversa o utilidad_buscadora si quieres

# ------------------------------
# Evaluación de utilidad esperada óptima (DP con memo)
# ------------------------------
def es_terminal(nodo):
    return nodo not in grafo or len(grafo[nodo]) == 0

def valor_terminal(nodo):
    return U(recompensa_terminal.get(nodo, 0))

def mejor_decision(nodo, horizonte=5, gamma=1.0, memo=None, politica=None):
    """
    Retorna (valor_optimo, accion_optima)
    - horizonte: profundidad máxima restante (para evitar bucles en grafos grandes).
    - gamma: factor de descuento (0..1).
    """
    if memo is None:
        memo = {}
    if politica is None:
        # mapa nodo -> acción óptima (se puede rellenar fuera si se desea)
        politica = {}

    clave = (nodo, horizonte)
    if clave in memo:
        return memo[clave]

    # Si nodo terminal o se agotó el horizonte, valor = recompensa terminal
    if es_terminal(nodo) or horizonte == 0:
        v = valor_terminal(nodo)
        memo[clave] = (v, None)
        return memo[clave]

    mejor_v = -1e18
    mejor_a = None

    # Probar cada acción disponible
    for accion, outcomes in grafo[nodo].items():
        # Utilidad esperada de esta acción:
        # sum p * ( U(recompensa_inmediata) + gamma * V*(siguiente) )
        ue = 0.0
        for (siguiente, p, r) in outcomes:
            v_next, _ = mejor_decision(siguiente, horizonte-1, gamma, memo, politica)
            ue += p * ( U(r) + gamma * v_next )

        if ue > mejor_v:
            mejor_v = ue
            mejor_a = accion

    memo[clave] = (mejor_v, mejor_a)
    return memo[clave]

def politica_optima(inicio, horizonte=5, gamma=1.0):
    """
    Recorre estados desde 'inicio' siguiendo la acción óptima,
    devolviendo (valor_esperado, lista_de_pasos).
    Nota: en nodos no terminales, solo guardamos la acción óptima.
    """
    memo = {}
    pasos = []
    nodo = inicio
    depth = horizonte

    while True:
        v, a = mejor_decision(nodo, depth, gamma, memo)
        if a is None:
            # terminal o sin horizonte
            pasos.append((nodo, 'terminal', 0.0))
            return v, pasos
        pasos.append((nodo, a, v))
        # Elegimos un "siguiente" simbólico (no hay transición real sin azar);
        # aquí solo devolvemos la política, no simulamos el resultado aleatorio.
        # Para mostrar la política, nos quedamos en el nodo actual y terminamos.
        # Si quieres simular, deberías muestrear por probabilidad p.
        # Cerramos aquí devolviendo solo la decisión en este nodo.
        return v, pasos

# ------------------------------
# Ejemplo de uso
# ------------------------------
if __name__ == "__main__":
    inicio = 'A'
    gamma = 1.0       # sin descuento
    horizonte = 3     # suficiente para alcanzar terminales

    valor, pasos = politica_optima(inicio, horizonte, gamma)

    print("Función de utilidad usada:", U.__name__)
    print("Valor (utilidad esperada) desde", inicio, "=", round(valor, 4))
    print("Política (acción recomendada por estado visitado):")
    for (estado, accion, v) in pasos:
        if accion == 'terminal':
            print(f"  {estado}: [terminal], V*={round(v,4)}")
        else:
            print(f"  {estado}: tomar acción '{accion}'  (V*≈ {round(v,4)})")
