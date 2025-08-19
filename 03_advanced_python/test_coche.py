"""
Archivo: 02_test_coche.py
Carpeta: 03_advanced_python

Ejemplos de uso de la clase Coche:
- Creación de objetos
- Aceleración y frenado
- Visualización de información
"""

from coche import Coche

# Crear un objeto de la clase Coche
coches = [
    Coche("Toyota", "Corolla", 2020),
    Coche("Honda", "Civic", 2019),
    Coche("Ford", "Mustang", 2021)
]

mi_coche = coches[0]
# Acelerar y frenar
mi_coche.acelerar()  # Acelera una vez
mi_coche.acelerar()  # Acelera otra vez
mi_coche.frenar()    # Frena una vez
mi_coche.frenar()    # Frena otra vez

# Mostrar información del coche
print(mi_coche.informacion())

# acelerar coches
for coche in coches:
    coche.acelerar()
    
# Frenar cada coche en la lista
for coche in coches:
    coche.frenar()

# Imprimir la información de cada coche
for coche in coches:
    print(coche.informacion())