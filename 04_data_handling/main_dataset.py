"""
Prueba de la clase DataSet:
- Mostrar datos y tipo
- Calcular media y mediana
"""

from dataset import DataSet

mi_dataset = DataSet([1, 2, 3, 4, 5])
print(mi_dataset.data)
print(mi_dataset.tipo_dato)

media = mi_dataset.media()
print(media)

mediana = mi_dataset.mediana()
print(mediana)