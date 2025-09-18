import time
class Contador:
    def __init__(self, cuenta_inicial):
        self.cuenta = cuenta_inicial

    def incrementar(self):
        self.cuenta += 1

    def obtener_cuenta(self):
        return self.cuenta
def main():
    try:
        valor_inicial = int(input("Ingresa el valor inicial del contador: "))
    except ValueError:
        contador = Contador(0)
    contador = Contador(valor_inicial)        

    for i in range(10):  
        print(f"Cuenta actual: {contador.obtener_cuenta()}")
        contador.incrementar()
        time.sleep(1)  # Pausa de 1 segundo entre incrementos
        
if __name__ == "__main__":
    main()