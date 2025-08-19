"""
Imprime el nombre del día de la semana según un número dado (1-7) usando match-case.
"""

numero_dia = 2

match numero_dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")