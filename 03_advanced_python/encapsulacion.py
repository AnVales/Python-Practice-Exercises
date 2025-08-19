"""
- Define la clase DataSet que utiliza encapsulación para proteger sus datos internos.
- Proporciona métodos para obtener estadísticas básicas (media, varianza) y para acceder a los datos de manera segura.
- Define una clase abstracta CalculadorEstadisticas que sirve como plantilla para calcular estadísticas específicas en clases derivadas.
"""
class DataSet:
    
    # uso interno por la _
    def __init__(self, data):
        self._data = data
        self._tamaño = len(data)
        
    def media(self):
        return sum(self.data) / self.tamaño
    
    def varianza(self):
        mu = self.media
        return sum((x-mu)**2 for x in self.data) / self.tamaño
    
    # devuelve una copia para proteger el original
    def obtener_data(self):
        return self._data.copy()
    
    
from abc import ABC , abstractmethod

class CalculadorEstadisticas(ABC):
    
    def __init__(self, data):
        self.data = data
    
    @abstractmethod        
    def calcular(self):
        pass