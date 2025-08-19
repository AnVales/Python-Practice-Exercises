"""
Función operacion_basica:
- Realiza suma, resta, multiplicación y división
- Controla división por cero
"""

def operacion_basica(a, b, operador):
    
    if operador == '+':
        return a + b    
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        if b != 0:
            return a / b
        else:
            return "Error, el divisor no puede ser 0"
        
    else:
        return "Operador no válido"    
    
# Uso de la función con diferentes argumentos
resultado_suma = operacion_basica(10, 5, '+')
resultado_resta = operacion_basica(10, 5, '-')
resultado_multiplicacion = operacion_basica(10, 5, '*')
resultado_division = operacion_basica(10, 5, '/')
resultado_division_cero = operacion_basica(10, 0, '/')

# Mostrar resultados
print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
print(f"División por cero: {resultado_division_cero}")