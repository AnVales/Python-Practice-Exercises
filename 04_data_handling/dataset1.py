"""
- Clase base `DataSet` que calcula la media de una lista numérica.
- Clase hija `DataSetPlus` que extiende la funcionalidad con la desviación estándar.
- Clase hija `DataSet8` que sobreescribe el método `media` para añadir un mensaje adicional.
"""
# clase padre
class DataSet:
    
    def __init__(self, data):
        self.data = data
        self.tamaño = len(data)
        
    def media(self):
        return sum(self.data) / len(self.data)

# clase hija    
class DataSetPlus(DataSet):
    
    def desviacion_estandar(self):
        mu = self.media()
        return (sum((x - mu) ** 2 for x in self.data) / self.tamaño) ** 0.5
    
class DataSet8(DataSet):
    
    def media(self):
        print("estoy calculando la media")
        return sum(self.data) / len(self.data)