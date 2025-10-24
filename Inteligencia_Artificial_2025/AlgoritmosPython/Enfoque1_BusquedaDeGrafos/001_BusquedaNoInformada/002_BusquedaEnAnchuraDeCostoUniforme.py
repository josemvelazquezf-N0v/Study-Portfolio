#Tambien conocido como Uniform Cost Search (UCS)

#"Este algoritmo busca por costos, no por niveles"

#Este es el grafo que usaremos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# #Se representa asi:
#      (1)        (5)
#   A ----> B --------> D
#    \       \
#    (4)      (2)
#     \        \
#      >-------> C ----> D (1)
#Este sistema de busqueda toma el camino mas "Facil" o el de menor coste
#Como se puede ver, cada camino tiene un valor el cual es su coste



#Iniciamos con el Main hasta arriba para que sea mas facil explicar la estructura del codigo
def Main():

    #Se llama a una funcion hecha para esta busqueda, donde se daran 3 parametros y se regresaran 2, uno el camino y el otro el costo del camino tomado
    #Los parametros que se necesitaran seran. el Grafo, Inicio y Objetivo
    #Este tipo de busqueda no puede funcionar con costos negativos, ya que podria generar bucles infinitos
    camino, costo = ucs_no_informada(grafo, 'A', 'D')
    print("Camino:", camino)     # ['A', 'B', 'C', 'D']
    print("Costo:", costo)       # 4


#Esta es la funcion nueva a la que se llama en el Main
def ucs_no_informada(grafo, inicio, objetivo):  #Aqui se pueden apreciar los parametros quee necesita
    
    #Condiciones Iniciales
    
    frontera = [(0, inicio)]                    #Primero inicia con el costo en 0 y el punto de inicio o (nodo) inicial
    mejor_costo = {inicio: 0}                   #Despues se busca el mejor costo, desde zero e inicio
    padre = {inicio: None}                      #Este guarda el camino que va tomando, desde inicio y ninguno (None) 
    #No se puede usar "0" en vez de None porque 0 es un valor numerico y no se puede usar con la logica de padres                    


#Bucle en donde se realizara la busqueda
    while frontera:
        # Sacar el nodo con el costo acumulado más bajo
        costo, nodo = pop_min(frontera)  #Lo agarra de una lista

        # Entradas obsoletas (ya tenemos una mejor)
        if costo > mejor_costo.get(nodo, float("inf")): #Si el costo es mayor al mejor costo guardado, se ignora
            continue
        # Si es la meta, este es el camino óptimo (sin heurística y costos >= 0)
        if nodo == objetivo:
            return reconstruir_camino(padre, objetivo), costo   #Se termina la funcion

        #Ahora ve los vecinos del nodo actual
        for vecino, w in grafo.get(nodo, []):
            if w < 0:   #Condicion de seguridad, solo por si el valor del costo es negativo
                raise ValueError("UCS requiere costos NO negativos.")
            nuevo = costo + w
            if nuevo < mejor_costo.get(vecino, float("inf")):   #Si el costo es mas pequeño que el mejor costo guardado
                mejor_costo[vecino] = nuevo                     #se cambia el mejor costo
                padre[vecino] = nodo                            #Se guarda el padre del nodo vecino como el nodo actual
                frontera.append((nuevo, vecino))                #Se agrega a la frontera el nuevo costo y el vecino
    return None, None #Si no se encuentra camino, regresa None

def reconstruir_camino(padre, objetivo):
    #Reconstruye el camino usando el mapa de padres.
    if objetivo not in padre:
        return None
    camino, cur = [], objetivo
    while cur is not None:
        camino.append(cur)
        cur = padre[cur]
    return list(reversed(camino))

def pop_min(frontera):
    #Saca (costo, nodo) con menor costo acumulado de una lista.
    if not frontera:
        return None
    idx = 0
    for i in range(1, len(frontera)):
        if frontera[i][0] < frontera[idx][0]:
            idx = i
    par = frontera[idx]
    frontera[idx:idx+1] = []   # elimina en O(n)
    return par  # (costo, nodo)



#Funcion solo para llamar al Main e iniciar el programa
if __name__ == "__main__":
    Main()

   
