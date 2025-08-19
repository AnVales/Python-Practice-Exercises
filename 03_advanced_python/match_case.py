"""
- Se clasifica el índice de masa corporal (IMC) en diferentes rangos.
- Se emplea 'case valor if ...' para aplicar condiciones específicas sobre el valor.
- El case _ maneja cualquier otro caso no válido.
"""
imc = 20

match imc:
    case valor if 0<valor<=18.5:
        print("bajo peso")
    case valor if 18.5 < valor <= 24.9:
        print("peso normal (saludable)")
    case valor if 24.9 < valor <= 34.9:
        print("obesiad clase 1 (moderada)")
    case valor if 34.9 < valor <= 39.9:
        print("obesiad clase 2 (severa)")
    case valor if 39.9 < valor:
        print("obesiad clase 3 (muy severa)")
    case _:
        print("valores de IMC no validos")
