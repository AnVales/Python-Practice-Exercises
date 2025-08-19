"""
Ejercicio de Python:
- Definición de clases y objetos
- Atributos y métodos de instancia
- Simulación de un coche con aceleración y frenado
"""

class Coche():
    
    # Atributos
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
        
    # Metodos
    def acelerar(self):
        if self.velocidad < 200:
            self.velocidad += 10
            print(f"{self.marca} {self.modelo} está acelerando. Velocidad: {self.velocidad} km/h")
        else:
         print(f"{self.marca} {self.modelo} no puede acelerar más. Velocidad: {self.velocidad} km/h")
           
    def frenar(self):
        
        if self.velocidad <= 10:
            self.velocidad = 0
            print(f"{self.marca} {self.modelo} está parado.")
        elif self.velocidad > 10:
            self.velocidad -= 10
            print(f"{self.marca} {self.modelo} está frenando. Velocidad: {self.velocidad} km/h")
        
    def informacion(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Velocidad actual: {self.velocidad} km/h"
        