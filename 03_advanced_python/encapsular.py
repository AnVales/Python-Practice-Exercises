"""
- Clase CuentaBancaria que utiliza encapsulación para proteger los atributos del titular y el saldo.
- Métodos públicos para depositar, retirar dinero y mostrar información de manera segura.
- Demuestra cómo interactuar con atributos privados usando getters y operaciones controladas.
"""

class CuentaBancaria:
    
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad}€. Saldo actual: {self.__saldo}€.")
        else:
            print(f"No se puede depositar dinero negativo")
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad}€. Saldo actual: {self.__saldo}€.")
        else:
            print(f"No se puede retirar dinero negativo")
            
    def mostrar_saldo(self):
        return f"El saldo actual es de {self.__saldo}€"
    
    def mostrar_titular(self):
        return f"El titular es {self.__titular}"
    
    
# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("Carlos", 1000)

# Uso de los métodos públicos para interactuar con los atributos privados
print(cuenta.mostrar_titular())
print(cuenta.mostrar_saldo())
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.mostrar_saldo())
