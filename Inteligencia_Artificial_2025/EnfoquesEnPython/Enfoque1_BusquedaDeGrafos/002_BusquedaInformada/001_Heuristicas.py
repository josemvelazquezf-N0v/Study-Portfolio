


# Grafo con costos (no se usan directamente en este heurístico simple)
grafo = {
    'A': [('B', 1), ('C', 4), ('D', 3)],
    'B': [('E', 2), ('F', 3)],
    'C': [('G', 2)],
    'D': [('H', 4)],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

#           (A)
#         /  |  \
#      1 /   |4  \3
#       /    |    \  
#     (B)   (C)   (D)
#     | \     \     \
#    2| 3\     2\     4
#     |    \     \     \
#    (E)   (F)   (G)   (H)




# Heurísticas h(n): estimación de la distancia restante a la meta G
heuristica = {
    'A': 7,
    'B': 6,
    'C': 1,
    'D': 4,
    'E': 5,
    'F': 3,
    'G': 0,
    'H': 6
}

def busqueda_heuristica(grafo, heuristica, inicio, meta):
    frontera = [inicio]
    visitados = []

    while frontera:
        # Selecciona el nodo con menor heurística
        nodo_actual = min(frontera, key=lambda n: heuristica[n])
        frontera.remove(nodo_actual)
        print(f"Visitando {nodo_actual} (h={heuristica[nodo_actual]})")

        if nodo_actual == meta:
            print("Meta encontrada ✅")
            return visitados + [nodo_actual]

        visitados.append(nodo_actual)

        # Agrega vecinos no visitados
        for vecino, _ in grafo.get(nodo_actual, []):
            if vecino not in visitados and vecino not in frontera:
                frontera.append(vecino)

    return None

# ========================
# Ejemplo de uso
# ========================
inicio = 'A'
meta = 'G'
camino = busqueda_heuristica(grafo, heuristica, inicio, meta)

print("\nCamino encontrado (orden de visita):", " -> ".join(camino))
