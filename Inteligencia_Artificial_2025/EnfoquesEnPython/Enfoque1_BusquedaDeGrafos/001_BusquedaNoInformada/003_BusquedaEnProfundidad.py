# Tambien conodico como Depth-First Search (DFS)

# Grafo como lista de adyacencia (dirigido)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#Se representa asi:
#       A
#      / \
#     B   C
#    / \   \
#   D   E__>F

#Se puede notar explora de manera profunda, pero esto hace que cuando llega a un camino
#ya se queda con este y no busca otros caminos, como A->C->F, que es mas corto que A->B->E->F
def main():
    orden = dfs_recorrido(grafo, 'A')
    print("Orden DFS:", orden)                      #   Es el proceso de visita: A, B, D, E, F, C

    camino = dfs_buscar_camino(grafo, 'A', 'F')    
    print("Camino A→F:", camino)                    #   A->B->E->F   


def dfs_recorrido(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = []
    visitados.append(inicio)
    # Procesa el nodo (ej. imprimir)
    print("Visito:", inicio)
    # Explora vecinos
    for v in grafo.get(inicio, []):
        if v not in visitados:
            dfs_recorrido(grafo, v, visitados)
    return visitados

def dfs_buscar_camino(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None: visitados = set()
    if camino is None: camino = []

    visitados.add(inicio)
    camino.append(inicio)

    if inicio == objetivo:
        return camino[:]  # copia (encontrado)

    for v in grafo.get(inicio, []):
        if v not in visitados:
            res = dfs_buscar_camino(grafo, v, objetivo, visitados, camino)
            if res is not None:
                return res

    # backtrack
    camino.pop()
    return None

if __name__ == "__main__":
    main()
