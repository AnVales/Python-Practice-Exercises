"""
Ejercicio de diccionarios en Python:
- Crear y actualizar diccionarios
- Modificar y eliminar elementos
- Ordenar diccionarios por claves
"""

from collections import OrderedDict

# Crear un diccionario con información sobre cinco productos y sus cantidades.
inventario = {
    "manzanas": 10,
    "naranjas": 15,
    "bananas": 20,
    "peras": 12,
    "uvas": 18
}

# Añadir dos nuevos productos al diccionario.
inventario.update({'cereza': 2, 'frambuesa': '20'})

inventario["manzanas"] = 1
inventario["bananas"] = 1
print(inventario)

# Eliminar dos productos del diccionario.
inventario.pop('uvas', 'Clave no encontrada')
inventario.pop('naranjas', 'Clave no encontrada')

# Mostrar todos los productos y sus cantidades, ordenados por nombre del producto.
print("Productos y cantidades ordenados por nombre del producto:")
for producto in sorted(inventario):
    print(f"{producto}: {inventario[producto]}")