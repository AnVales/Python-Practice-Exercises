"""
Ejercicio de manipulación de listas en Python:
- Crear una lista
- Agregar elementos
- Insertar en posiciones específicas
- Eliminar elementos
- Ordenar ascendente y descendente
"""

lista = [4, 8, 15, 16, 23, 42]
print(lista)

# Agregar un número al final de la lista.
lista.append(2)
print(lista)

# Insertar un número en una posición específica.
lista.insert(3, 4)
print(lista)

# Eliminar un numero de la lista
lista.pop(0)
print(lista)

# Encontrar y eliminar un número específico de la lista.
lista.remove(4)
print(lista)

# ordenar en orden ascendente
lista.sort()
print(lista)

# ordenar en orden descendente
lista.sort(reverse=True)
print(lista)