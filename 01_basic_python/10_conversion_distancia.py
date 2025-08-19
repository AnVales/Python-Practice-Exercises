"""
Ejercicio de funciones en Python:
- Definir funciones
- Retornar múltiples valores (metros, millas, centímetros)
- Uso de funciones para cálculos simples
"""

# Definir la función convertir_distancia.
def convertir_distancia(km):
    
    # metros
    metro = km*1000
    
    # millas
    millas = km*0.621371 
    
    # centímetros
    centimetros = km*100000
    
    return metro, millas, centimetros
      
km = 96
m, milla, cm = convertir_distancia(km) 
print(m)
print(milla)
print(cm)  