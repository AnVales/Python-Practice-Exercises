"""
- Define SaldoInsuficienteError como excepción específica.
- La clase CuentaBancaria usa esta excepción para controlar retiros mayores al saldo.
- Demuestra el uso de try, except y finally para manejar errores de forma segura.
"""
class SaldoInsuficienteError(Exception):
    def __init__(self, message="Saldo insuficiente para completar la operación."):
        self.message = message
        super().__init__(self.message)

# Clase CuentaBancaria que usa la excepción personalizada
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}€. Saldo actual: {self.saldo}€.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(f"No puedes retirar {cantidad}€. Saldo actual: {self.saldo}€.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}€. Saldo actual: {self.saldo}€.")

# Crear una instancia de CuentaBancaria y probar el manejo de la excepción personalizada
cuenta = CuentaBancaria("Carlos", 100)

# Realizar operaciones con manejo de excepciones
try:
    cuenta.depositar(50)
    cuenta.retirar(30)  # Operación válida
    cuenta.retirar(150)  # Esta operación lanzará la excepción personalizada
except SaldoInsuficienteError as e:
    print(e)
finally:
    print("Operación finalizada.")

    