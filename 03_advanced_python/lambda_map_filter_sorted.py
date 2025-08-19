"""
Ejercicio de Python:
- Funciones lambda
- Uso de map, filter y sorted con lambda
"""

# funcion lambda

# lambda argumentos : expresion

suma = lambda a, b: a + b
print(suma(5,6))

# se usan como argumentos para funciones de orden superior

numeros = list(range(1, 11, 1))

# map aplica la funcion a cada elemento de la lista
cuadrados = list(map(lambda x : x**2, numeros))
print(cuadrados)

# filter aplica la funcion y devuelve aquellos para los que la funcion sea verdadera
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# sorted ordena segun el criterio
frutas = ['fresa', 'manzana' 'banana', 'cereza']
frutas_ordenadas = sorted(frutas, key=lambda fruta: len(fruta))
print(frutas_ordenadas)