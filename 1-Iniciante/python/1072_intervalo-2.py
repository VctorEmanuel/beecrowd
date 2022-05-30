n = int(input())
numeros = []
inn, out = 0, 0

for X in range(n):
    numeros.append(int(input()))

for numero in numeros:
    if 10 <= numero <= 20:
        inn += 1
    else:
        out += 1

print(f'{inn} in\n{out} out')