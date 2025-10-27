#Tambien conocido como Búsqueda en Profundidad Iterativa (IDDFS)


grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F
    #    /
    #   G



# DLS limitada (se usa dentro del IDDFS)

def dfs_limitado(grafo, nodo, objetivo, limite, profundidad=0):
    print(f"Visitando {nodo} (profundidad {profundidad})")
    
    if nodo == objetivo:
        return [nodo]
    if profundidad == limite:
        return None

    for vecino in grafo.get(nodo, []):
        camino = dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1)
        if camino is not None:
            return [nodo] + camino

    return None

# ------------------------------------------------------------
# Búsqueda en Profundidad Iterativa (IDDFS)
# ------------------------------------------------------------
def iddfs(grafo, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):
        print(f"\n--- Iteración con límite {limite} ---")
        camino = dfs_limitado(grafo, inicio, objetivo, limite)
        if camino:
            return camino, limite
    return None, None

# ------------------------------------------------------------
# Ejemplo de uso
# ------------------------------------------------------------
inicio = 'A'
meta = 'G'
limite_maximo = 5

camino, profundidad_encontrada = iddfs(grafo, inicio, meta, limite_maximo)

print("\nResultado final:")
if camino:
    print(f"Camino encontrado: {' -> '.join(camino)} (profundidad {profundidad_encontrada})")
else:
    print("No se encontró la meta dentro del límite máximo.")
