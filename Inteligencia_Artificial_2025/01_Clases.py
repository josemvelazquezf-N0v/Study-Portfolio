# Codigo de ejecucion en terminal: python3 01_Clases.py
#Asi se hacen las clases en Python
class Clase(): #
    def __init__(self): #Constructor de la clase
    #   Los constructores de una clase son elementos que sirven para al momento de iniciar una clase
    #   esta pueda declarar variables iniciales, mejor conocidos como artibutos
        self.atributo_1 = "Valor 1"
        self.atributo_2 = "Valor 2"
        
    #   Despues siguen los metodos(funciones de la clase):
    def metodo_1(self): #El self es para referirse a la misma clase, haciendo que los metodos y atributos puedan ser usados
        print("\nMetodo de clase 1:")
        print(self.atributo_1) #Ejemplo de uso del self para llamar un atributo de la clase
    #   Los metodos se dibiden de esta manera
    def metodo_2(self):
        print("\nMetodo de clase 2:")
        print(self.atributo_2)

def main():
    Clase1 = Clase() #Creacion de un objeto de la clase
    Clase1.metodo_1() #Uso del metodo 1
    Clase1.metodo_2() #Uso del metodo 2
    
#   Programa un poco basico, muestra la estructura de las clases y como se ejecutan atributos y metodos con ella
#   este tupo de clases pueden tener nombre cualquiera y atributos cualquiera
#   las clases son medios para clasificar y organizar codigo , puedes tener muchas clases de un mismo tipo y modificarlas
#   esto sirve para tener un codigo mas limpio y reutilizable, por ejemplo:
    
    Clase2 = Clase()
    Clase2.atributo_1 = "Nuevo Valor 1"
    Clase2.metodo_1()
    Clase2.metodo_2()

#   En esta parte se usa la misma clase y se modifica un atributo
#   ahora hay diferenciacion entre la clase 1 y la clase 2, no solo el nombre si no que el valor de uno de sus atributos
#   cambio, esto sirve mmucho para reutilizar codigo

if __name__ == "__main__":  #Es una condición especial en Python. Verifica si el archivo se está ejecutando directamente (no importado como módulo).
    main()                  #llama a la función principal solo si la condición anterior es verdadera.

