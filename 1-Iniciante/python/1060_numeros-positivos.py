numeros = []
ns = 0
for x in range(6):
    numeros.append(int(input()))
for numero in numeros:
    if numero > 0: ns += 1
print(f'{ns} valores positivos')
