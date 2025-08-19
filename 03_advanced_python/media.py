"""
Ejercicio de Python:
- Definir funciones para cálculos estadísticos
- Calcular la media (promedio) de los elementos de una lista
- Retornar el resultado y mostrarlo por pantalla
"""

def calcular_media(lista):
    suma = 0
    
    for i in lista:
        suma += i
    
    return suma/(len(lista))


lista1 = [1,2,3]
resultado = calcular_media(lista1)
print(resultado)
        
    
    