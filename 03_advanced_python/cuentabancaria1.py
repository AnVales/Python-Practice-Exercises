# Script de prueba de la clase CuentaBancaria
# Crea una cuenta, realiza depósitos y retiros, y muestra el saldo

from cuentabancaria import CuentaBancaria

cuenta1 = CuentaBancaria('Pepe', 2000)
print(cuenta1.depositar(10))
print(cuenta1.retirar(10))
print(cuenta1.mostrar_saldo)