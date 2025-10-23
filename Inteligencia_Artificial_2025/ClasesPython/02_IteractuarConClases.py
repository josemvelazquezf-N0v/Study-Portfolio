import time     #Libreria de tiempo, esta la usaremos despues, pero no tiene nada que ver con clases
class Contador: #Se define la clase

    cuenta = 0    #Se guarda el valor dado en un atributo (cuenta)

    def incrementar(self):  #Metodo para incrementar la cuenta
        self.cuenta += 1    #se incrementa de 1 en 1

    def obtener_cuenta(self):   #Metodo para obtener el valor actual de la cuenta
        return self.cuenta      #Retorna el valor actual de la cuenta

def main():             #Codico main 
    try:                #Funcion de python, intenta hacer una accion, en el caso de que falle hace lo que dice "except"
        valor_inicial = int(input("Ingresa el valor inicial del contador: "))   #Pude un valor numerico, si se ingresa algo como un texto, fallara
        contador = Contador()                                   #Aqui se declara el objeto contador
        contador.cuenta = valor_inicial                         #Se asigna el valor inicial al atributo cuenta
    except ValueError:                                          #Este es el "except", si falla la parte de arriba, hace lo siguiente
        contador = Contador()                                    #Si falla, inicia el contador en 0
           
    for i in range(10):                                         #Un for, va a hacer el ciclo 10 veces
        print(f"Cuenta actual: {contador.obtener_cuenta()}")    #Muestra el valor actual de la cuenta
        contador.incrementar()                                  #Incrementa la cuenta con el metodo
        time.sleep(1)                                           #Para esto use la libreria "time" para hacer una pausa de 1 segundo 
        
if __name__ == "__main__":                                      #Funcion main, de python base
    main()