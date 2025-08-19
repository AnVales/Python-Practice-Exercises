"""
- Crear una lista y transformarla en tupla y conjunto.
- Uso de operaciones básicas de conjuntos: agregar, eliminar, verificar pertenencia.
- Realizar unión e intersección entre conjuntos.
"""
# Crear una lista de números del 1 al 10.
lista_1 = list(range(1,11))
print(lista_1)

# Convertir la lista en una tupla.
tupla_1 = tuple(lista_1)
print(tupla_1)

# Crear un conjunto con los elementos de la tupla.
conjunto_1 = set(tupla_1)
print(conjunto_1)

# Agregar un nuevo elemento al conjunto.
conjunto_1.add(1) 
print(conjunto_1)

# Eliminar un elemento del conjunto.
conjunto_1.discard(1)
print(conjunto_1)

# Verificar si un elemento está en el conjunto.
existe_cinco = 5 in conjunto_1
print(existe_cinco)

# Unir dos conjuntos y obtener la intersección.
conjunto_2 = {0, 8, 6, 5, 7, 1}
print(conjunto_2)

conjunto_unido = conjunto_1 & conjunto_2
print(conjunto_unido)

conjunto_interseccion = conjunto_1 | conjunto_2
print(conjunto_interseccion)