"""
Ejercicio de algoritmos en Python:
- Definir funciones
- Verificar si un número es primo
- Uso de bucles y condicionales
- Uso de la biblioteca math para optimización
"""
import math as mth

def es_primo(num):
    if num<2:
        return False
    for i in range(2, int(mth.sqrt(num))+1):
        if i % num == 0:
            return False
    return True


solucion = es_primo(5) 
print(solucion)  
        
        