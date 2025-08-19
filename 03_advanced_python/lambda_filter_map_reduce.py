"""
Ejercicio de funciones lambda en Python:
- Uso de lambda con filter, map y reduce
- Filtrar, transformar y reducir listas
"""

# lambda argumentos : expresion

from functools import reduce

# Filtrar los números pares.
numeros = list(range(1, 11))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# Elevar al cuadrado cada número.
numeros_cuadrados = list(map(lambda x: x**2, numeros_pares))
print(numeros_cuadrados)

# Sumar todos los números elevados al cuadrado.
suma_numeros = reduce(lambda x, y: x + y, numeros_cuadrados)
print(suma_numeros)