numeros = list (range(1, 21))

for i in numeros:
    
    if i==15:
        break 
    if i % 2 == 0:
        continue
    else:
        print(i)