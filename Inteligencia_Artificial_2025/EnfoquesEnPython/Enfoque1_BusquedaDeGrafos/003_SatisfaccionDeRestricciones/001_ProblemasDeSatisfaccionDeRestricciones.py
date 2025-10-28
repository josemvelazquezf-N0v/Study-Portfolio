# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

#       (A)
#      /   \
#    (B) - (C)
#      \   /
#       (D)

# Se les va a asignar colores a los nodos A, B, C, D
# de tal forma que nodos adyacentes no tengan el mismo color.




# Colores posibles
colores = ['Rojo', 'Verde', 'Azul']

# ------------------------------------------------------
# Verifica si es válido asignar 'color' al nodo 'nodo'
# ------------------------------------------------------
def es_valido(nodo, color, asignacion):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False  # Violación de restricción
    return True

# ------------------------------------------------------
# Algoritmo recursivo de backtracking para CSP
# ------------------------------------------------------
def colorear_grafo(asignacion, nodos):
    # Si todos los nodos tienen color → éxito
    if len(asignacion) == len(nodos):
        return asignacion

    # Escoge un nodo sin asignar
    nodo = [n for n in nodos if n not in asignacion][0]

    # Prueba cada color del dominio
    for color in colores:
        if es_valido(nodo, color, asignacion):
            asignacion[nodo] = color
            resultado = colorear_grafo(asignacion, nodos)
            if resultado:
                return resultado
            # Retroceso
            del asignacion[nodo]

    return None  # No hay solución válida

# ------------------------------------------------------
# Ejecución
# ------------------------------------------------------
nodos = list(grafo.keys())
solucion = colorear_grafo({}, nodos)

print("\nAsignación de colores encontrada:")
if solucion:
    for nodo, color in solucion.items():
        print(f"  {nodo} → {color}")
else:
    print("No se encontró una coloración válida.")



#       (A:Rojo)
#      /       \
#  (B:Verde) - (C:Azul)
#      \       /
#       (D:Rojo)

#Se cumplio