#   Algoritmo de Busqueda en anchura, se usa un valor inicial al azar y se empieza a "Explorar"
#   en los valores vecinos a el valor inicial, despues se visitan todos los nodos a 2 pasos de distancia
#   luego se sigue explorando separandose del valor inicial

#   Es un algoritmo de Busqueda no informada porque no tienes informacion sobre el objetivo que se quiere llegar
#   por ello el primer valor es al azar y desde ahi se explora hasta llegar al objetivo

#   No "sirve" para deducir funciones o predecir valores, es un algoritmo que se encarga de encontrar un valor que
#   satisfaga un cierto criterio, por ello la busqueda en anchura busca un valor "Adecuado" de manera rapida, no predice

# Ok, pedi ejemplos a una IA y ahora los intentare explicar
# Lo siguente es un Grafo:
grafo = {
    'A': ['B', 'C', 'E'],
    'B': [],
    'C': ['D'],
    'D': [],
    'E': []
}
# Representa 5 nodos, A, B, C, D, E
# Existen conexiones entre estos, A esta conectado con B, C y E pero B, por ejemplo no esta conectado con nadie
# Esto representa que hay conexiones entre nodos y no todos son conexiones bidireccionales
# El grado se puede representar graficamente como:
#       A
#     / | \
#    B  C  E
#       |
#       D
# El algortimo de anchura primero empezaria en A y se iria extendiendo primero a sus vecinos B, C y E
# Luego iria a los vecinos a 2 pasos de A, ahora seria a: D




#Se supone que el algoritmo de busqueda usa listas, donde agrega primero a los vecinos y despues a los vecinos de los vecinos
#Descartando los nodos ya visitados por lo que no se vuelven a mostrar
def bfs(inicio):
    visitados = []          # Lista de nodos ya visitados
    cola = [inicio]         # Cola con el nodo inicial

    while cola:             # Mientras haya nodos por explorar
        nodo = cola.pop(0)  # Sacamos el primero en la cola

        if nodo not in visitados:
            print(f"Visitando: {nodo}")
            visitados.append(nodo)  # Marcamos como visitado

            # Agregamos sus vecinos al final de la cola
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

    return visitados
#Se supone que visita los nodos en el orden en el que se pusieron en el grafo
#Como "A" contiene "B", "C" y "E" primero visitara esos nodos
#Luego visitara "B", pero no hay ninguna conexion, entonces seguira con "C"
#Luego visitara "D" porque es contenido por "C", seguira en "D", pero no tiene conexiones
#Finalmente visitara "E", pero como no tiene vecinos no visitará nada mas, en las dobles visitas no hara nada
#Porque ya fueron descartados porque ya estaban en la lista de visitados

# Ejecutamos la búsqueda
orden = bfs('A')
print("Orden de recorrido:", orden)


