"""
Ejercicio de Python:
- Separar cadenas usando split()
- Uso de match-case para operaciones aritméticas
- Definir funciones para calcular resultados
"""
suma = "2 + 2"
multiplicacion = "5 * 3"

def match_mult(mult):
    split_mult = mult.split()
    
    match split_mult:
        case [str(a), "+", str(b)]:
            return int(a)+int(b)
        case [str(a), "-", str(b)]:
            return int(a)-int(b)
        case [str(a), "*", str(b)]:
            return int(a)*int(b)
        case [str(a), "/", str(b)]:
            return int(a)/int(b)
        case _:
            return "No válido"
    
    
    
print(match_mult(suma))