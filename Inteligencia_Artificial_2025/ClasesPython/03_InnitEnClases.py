#En este caso se muestra como iniciar una clase en python
#Explicare a fondo la el metodo "def __init__" en las clases 

class SinInnit:
    x = 1
    y = 2
    z = 3
    def mostrar():
        print(f"x: {SinInnit.x}, y: {SinInnit.y}, z: {SinInnit.z}")

class ConInnit:
    def __init__(self, x, y, z):    #El metodo init es un constructor, este se ejecuta al momento de crear el objeto
        self.x = x                  #Aqui se definen los atributos de la clase, en este caso son 3 (x,y,z) y yo les di el valor al momento de crear el objeto
        self.y = y
        self.z = z
    def mostrar(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")

def main():
    #Ahora se veran las diferencias entre las clases
    clase1 = SinInnit  #Aqui se crea el objeto de la clase sin init
    clase2 = ConInnit(10,20,30) #Aqui se crea el objeto de la clase con init, y se le dan los valores a los atributos
    clase3 = ConInnit(100,200,300) #Se puede crear otro objeto de la misma clase con diferentes valores

    clase1.mostrar() #Se muestra el objeto sin init, los valores son los que se definieron en la clase
    clase2.mostrar() #Se muestra el objeto con init, los valores son los que se le dieron al momento de crear el objeto
    clase3.mostrar() #La tercera clase esta para mostrar la versatilidad de la declaracion con init

    #La clase sin init solo puede tener un valor base de inicio y si se quiere modificar se tendra que hacer lo siguente
    clase4 = SinInnit
    clase4.x = 10
    clase4.y = 20
    clase4.z = 30
    clase4.mostrar() #Aqui se muestra la clase sin init pero con los valores modificados

    #Ayuda a la versatilidad, tanto de reuso como para modificar parametros al programar y querer reajustar algo

if __name__ == "__main__":
    main()