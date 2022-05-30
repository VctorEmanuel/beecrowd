numeros = []
for x in range(100):
    numeros.append(int(input()))

print(f'{max(numeros)}\n{numeros.index(max(numeros)) + 1}')