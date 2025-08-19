"""
Ejemplo de uso de variables locales y globales:
- Definición de variables globales
- Funciones para agregar, eliminar y mostrar productos en un inventario global
"""

# Variables locales y globales

# Definir una variable global para el inventario
inventario = []

# Definir funciones para agregar, eliminar y mostrar productos en el inventario global.
def agregar_producto(producto):
    global inventario
    inventario.append(producto)
    print(f"Producto '{producto}' agregado al inventario.")
    
agregar_producto('limones')

def eliminar_producto(producto):
    global inventario
    if producto in inventario:
        eliminado = inventario.remove(producto)
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print(f"Producto '{producto}' no está en inventario.")
    
eliminar_producto('limones')

def mostrar_inventario():
    global inventario
    print('El inventario es:', inventario)
    
agregar_producto('galletas')
mostrar_inventario()