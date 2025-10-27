# Grafo no dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['E', 'F']
}


    #       A
    #     /   \
    #    B     C
    #   / \     \
    #  D   E     F
    #       \   /
    #         G


def busqueda_en_grafos(grafo, inicio, meta):
    frontera = [inicio]       # Cola o pila según el tipo de búsqueda
    visitados = set([inicio]) # Para no repetir nodos
    padre = {inicio: None}    # Para reconstruir camino

    while frontera:
        nodo = frontera.pop(0)  # pop(0) → comportamiento BFS (cola FIFO)
        print(f"Visitando: {nodo}")

        if nodo == meta:
            return reconstruir_camino(padre, meta)

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = nodo
                frontera.append(vecino)

    return None  # Si no se encontró la meta

def reconstruir_camino(padre, meta):
    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    return list(reversed(camino))

# Ejemplo de uso
camino = busqueda_en_grafos(grafo, 'A', 'G')
print("\nCamino encontrado:", " -> ".join(camino))
