"""
Clase en Python con atributos de clase y de instancia
atributo_de_clase: un atributo compartido por todas las instancias de la clase.
__init__: constructor que inicializa los atributos de instancia (parametro1 y parametro2) para cada objeto creado.
metodo_de_instancia: método que opera sobre los atributos de la instancia y devuelve su suma.
Ejemplo de uso: se crea un objeto obj con valores 3 y 7, se llama al método de instancia y se accede al atributo de clase directamente desde la clase.
"""
class NombreDeClase:
    atributo_de_clase = 10
    
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        
    def metodo_de_instancia(self):
        return self.parametro1 + self.parametro2

# Crear instancia
obj = NombreDeClase(3, 7)
print(obj.metodo_de_instancia())  # Salida: 10
print(NombreDeClase.atributo_de_clase)  # Salida: 10