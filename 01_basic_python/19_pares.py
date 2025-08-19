"""
Ejercicio básico de Python:
- Crear listas
- Iterar sobre listas con for
- Filtrar números pares usando condicionales
"""
numeros = [0, 1, 2, 3, 4, 5, 6, 7]
numeros_pares = []

for i in numeros:
    if i % 2 ==0:
        numeros_pares.append(i)
        
print(numeros_pares)