"""
- Función dividir_numeros que realiza división segura.
- Captura errores de división por cero y tipos de datos inválidos.
- Usa try, except, else y finally para un control completo del flujo.
"""

def dividir_numeros(a, b):
    try:
        # Intentar realizar la división
        resultado = a / b
        
    except ZeroDivisionError:
        # Manejar la excepción de división por cero
        print("Error: No se puede dividir por cero.")
    
    except TypeError:
        # Manejar la excepción de tipo de datos no válido
        print("Error: Los valores proporcionados deben ser números.")
    
    else:
        # Si no hay excepciones, mostrar el resultado
        print(f"El resultado de {a} / {b} es {resultado}")
    
    finally:
        # Mensaje que siempre se muestra al final
        print("Operación de división finalizada.")
        
# Llamadas a la función con diferentes casos
dividir_numeros(10, 2)  # División válida
dividir_numeros(10, 0)  # División por cero
dividir_numeros(10, 'a')  # Tipo de dato no válido