"""
Ejercicio de tuplas en Python:
- Crear tuplas
- Acceder a elementos
- Manejar errores al modificar tuplas
- Concatenar tuplas
- Verificar existencia de elementos
- Desempaquetar tuplas
"""

# Crear una tupla con los elementos (10, 20, 30, 40, 50).
tupla = (10, 20, 30, 40, 50)

# Acceder al tercer elemento de la tupla
terer_elemento = tupla[3]
print(terer_elemento)

# Intentar modificar un elemento de la tupla y capturar la excepción.
try:
    tupla[0] = 100
except TypeError as e:
    print(f"Error al intentar modificar la tupla: {e}")
    
# Concatenar la tupla original con otra tupla (60, 70, 80).
tupla_2 = (60, 70, 80)
tupla_unida = tupla + tupla_2
print(tupla_unida)

# Verificar si un elemento (por ejemplo, 40) existe en la tupla concatenada.
elemento = 40
print(elemento in tupla_unida)

# Desempaquetar los primeros tres elementos de la tupla concatenada en variables separadas.
a, b, c = tupla[:3]
print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3