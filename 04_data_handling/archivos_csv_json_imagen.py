"""
Ejercicio de manejo de datos en Python:
- Archivos CSV: escritura y lectura
- Archivos JSON: serialización y deserialización
- Manipulación básica de imágenes con PIL
"""

import csv

with open('datos.csv', mode='w') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['nombre', 'edad', 'ciudad'])
    escritor.writerow(['Alice', '30', 'Nueva York'])
    escritor.writerow(['Juan', '34', 'Quito'])
    
with open('datos.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
        
import json

with open('data.json', 'w') as archivo:
    json.dump({'nombre': 'Alice', 'edad': 30}, archivo)
    
with open('data.json', 'r') as archivo:
    datos = json.load(archivo)
    print(datos)
    
from PIL import Image

imagen = Image.open('flor.jpg')
imagen.show()
imagen_gris = imagen.convert('L')
imagen_gris.save('flor_gris.jpg')
imagen_gris.show()