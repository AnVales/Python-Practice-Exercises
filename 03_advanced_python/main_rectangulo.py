"""
Prueba de la clase Rectangulo:
- Crear instancias
- Calcular área y perímetro
- Verificar si es cuadrado
"""

from rectangulo import Rectangulo

rectangulo1 = Rectangulo(2, 3)
area = rectangulo1.area()
print(area)
perimetro = rectangulo1.perimetro()
print(perimetro)
print(rectangulo1.es_cuadrado())