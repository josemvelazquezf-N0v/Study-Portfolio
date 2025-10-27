# Grafo NO dirigido como lista de adyacencia.
# Para dirigido: provee también 'grafo_rev' (aristas invertidas).
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}
    #          A
    #        /   \
    #       /     \
    #      B       C
    #     / \       \
    #    D   E       F
    #         \     / \
    #          \   /   \
    #            F ----- G




def reconstruir_camino(padre_s, meeting, padre_t):
    """
    Une el camino desde s hasta 'meeting' (usando padre_s)
    con el camino desde 'meeting' hasta t (usando padre_t).
    padre_* guardan padres en su respectiva búsqueda.
    """
    # Parte s -> meeting
    izq = []
    cur = meeting
    while cur is not None:
        izq.append(cur)
        cur = padre_s.get(cur, None)
    izq.reverse()  # ahora va s ... meeting

    # Parte meeting -> t
    der = []
    cur = padre_t.get(meeting, None)  # evitar repetir 'meeting'
    while cur is not None:
        der.append(cur)
        cur = padre_t.get(cur, None)

    return izq + der  # camino completo s ... meeting ... t

def bidirectional_bfs(grafo, inicio, meta):
    if inicio == meta:
        return [inicio]

    # Estructuras para la búsqueda desde s (izquierda) y t (derecha)
    visit_s = set([inicio])
    visit_t = set([meta])
    padre_s = {inicio: None}
    padre_t = {meta: None}
    cola_s = [inicio]
    cola_t = [meta]

    while cola_s and cola_t:
        # Heurística: expandir la frontera más pequeña
        if len(cola_s) <= len(cola_t):
            meeting = _expand_layer(grafo, cola_s, visit_s, visit_t, padre_s, from_start=True)
        else:
            meeting = _expand_layer(grafo, cola_t, visit_t, visit_s, padre_t, from_start=False)

        if meeting is not None:
            # Encontramos intersección en 'meeting'
            return reconstruir_camino(padre_s, meeting, padre_t)

    return None  # No hay camino

def _expand_layer(grafo, cola, visit_self, visit_other, padre, from_start=True):
    """
    Expande una capa (un nivel) de BFS.
    - cola: frontera (lista) de esta dirección
    - visit_self: visitados de esta dirección
    - visit_other: visitados de la otra dirección
    - padre: padres de esta dirección
    Retorna el nodo de 'encuentro' si se halla; si no, None.
    """
    # Expandir todos los nodos del nivel actual
    nivel_count = len(cola)
    for _ in range(nivel_count):
        nodo = cola.pop(0)
        for v in grafo.get(nodo, []):
            if v not in visit_self:
                visit_self.add(v)
                padre[v] = nodo
                cola.append(v)
                if v in visit_other:
                    # Se encontró intersección
                    return v
    return None

# ======================
# Ejemplo de uso
# ======================
if __name__ == "__main__":
    camino = bidirectional_bfs(grafo, 'A', 'G')
    print("Camino A→G:", camino)
