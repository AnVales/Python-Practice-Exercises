"""
Ejercicio de Python:
- Calcular el factorial de un número usando un bucle while
- Retornar el resultado de la multiplicación acumulada
- Imprimir el factorial calculado
"""
def factorial(numero):
    resultado = 1
    
    while numero > 1:
        resultado *= numero
        numero -= 1
        
    return resultado

print(factorial(25))
