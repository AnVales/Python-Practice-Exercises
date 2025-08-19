"""
- La clase base Vehiculo define métodos generales como arrancar y detener.
- Las clases derivadas Coche y Motocicleta extienden Vehiculo y añaden comportamientos específicos.
- Demuestra cómo usar super() para inicializar la clase base y cómo acceder a métodos de la clase base y derivadas.
"""
class Vehiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def arrancar(self):
        return f"{self.marca} {self.modelo} ha arrancado."

    def detener(self):
        return f"{self.marca} {self.modelo} se ha detenido."

# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
        self.año = año
        
    def abrir_maletero(self):
         return f"{self.marca} {self.modelo} {self.año} ha abierto el maletero y lo ha cerrado"
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo)
        self.año = año
        self.tipo = tipo
    
    def hacer_caballito(self):
        return f"{self.marca} {self.modelo} {self.año} hace el caballito"
    
    
coche = Coche("Toyota", "Corolla", 2022, 4)
moto = Motocicleta("Harley-Davidson", "Sportster", 2021, "Cruiser")

# Usar métodos de la clase base
print(coche.arrancar())
print(moto.arrancar())

# Usar métodos específicos de las clases derivadas
print(coche.abrir_maletero())
print(moto.hacer_caballito())

# Usar otro método de la clase base
print(coche.detener())
print(moto.detener())