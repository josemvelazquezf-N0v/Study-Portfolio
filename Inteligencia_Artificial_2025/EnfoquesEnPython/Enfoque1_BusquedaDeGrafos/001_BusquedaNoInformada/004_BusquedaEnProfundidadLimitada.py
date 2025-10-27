#Tambien conocido como Depth-Limited Search (DLS)


# Grafo simple
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def dfs_limitado(grafo, nodo, objetivo, limite, profundidad=0):
    print(f"Visitando {nodo} (profundidad {profundidad})")

    # Caso base: encontramos la meta
    if nodo == objetivo:
        return [nodo]

    # Caso de corte: alcanzamos el límite
    if profundidad == limite:
        return None

    # Exploramos vecinos
    for vecino in grafo.get(nodo, []):
        camino = dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1)
        if camino is not None:
            return [nodo] + camino

    return None  # No se encontró dentro del límite

# ======================
# Ejemplo de uso
# ======================
inicio = 'A'
meta = 'G'
limite = 2

camino = dfs_limitado(grafo, inicio, meta, limite)

print("\nResultado:")
if camino:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print(f"No se encontró {meta} con límite de profundidad {limite}.")
