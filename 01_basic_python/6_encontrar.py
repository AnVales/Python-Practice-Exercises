"""
Ejemplo de búsqueda en una lista: recorre los elementos y detiene el ciclo al encontrar un valor específico.
"""
lista = [1, 2, 3, 4, 5]

for i in lista:
    if i == 3:
        print("encontrado", i)
        break