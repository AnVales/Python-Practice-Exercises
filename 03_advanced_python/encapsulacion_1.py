"""
- Demuestra encapsulación de datos usando una clase DataSet
- Acceso a los datos mediante un método público (obtener_data)
- Muestra que los atributos privados también existen, pero deberían ser accedidos solo mediante métodos de la clase
"""

from encapsulacion import DataSet

datos = DataSet([4, 3, 7])
datos_impresos = datos.obtener_data()
print(datos_impresos)
print(datos._data)

