# ================================
# TD(0) para grafos genéricos
# ================================

    #  +---+      +---+      +---+
    #  | A | ---> | B | ---> | C(+10)|
    #  +---+      +---+      +---+
    #    |                     ^
    #    v                     |
    #  +---+                   |
    #  | D | ------------------+
    #  +---+


import random

# Grafo dirigido: nodo -> {vecino: probabilidad}
grafo = {
    'A': {'B': 0.5, 'D': 0.5},
    'B': {'C': 1.0},
    'C': {},    # terminal
    'D': {'C': 1.0}
}

# Recompensas inmediatas
recompensas = {
    'A': 0,
    'B': 0,
    'C': 10,   # terminal positiva
    'D': 0
}

# Política fija (no se aprende todavía)
def politica_fija(nodo):
    if nodo not in grafo or len(grafo[nodo]) == 0:
        return None
    # elegir al azar según las probabilidades del grafo
    vecinos = list(grafo[nodo].keys())
    return random.choice(vecinos)

def td_grafo(gamma=0.9, alpha=0.1, episodios=1000):
    # Inicializa utilidades
    U = {nodo: 0.0 for nodo in grafo}

    for ep in range(episodios):
        s = 'A'  # estado inicial
        while True:
            if s not in grafo or len(grafo[s]) == 0:
                break  # estado terminal
            s2 = politica_fija(s)
            r = recompensas[s2]
            # TD(0)
            U[s] = U[s] + alpha * (r + gamma * U[s2] - U[s])
            s = s2
            if s2 not in grafo or len(grafo[s2]) == 0:
                break
    return U

# Ejecutar
U = td_grafo()
print("\nUtilidades aprendidas:")
for nodo, val in U.items():
    print(f"  {nodo}: {val:.3f}")
