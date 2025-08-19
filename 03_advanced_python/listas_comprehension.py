"""
Ejercicio de Python:
- Listas por comprensión
- Generadores
- Diccionarios por comprensión
"""

cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados)

cuadrados_set = (x**2 for x in range(10))
print(cuadrados_set)

cuadrados_dic = {x: x**2 for x in range(1, 5)}
print(cuadrados_dic)

lista = []
for x in range(10):
    lista.append(x**2)
    
print(lista)