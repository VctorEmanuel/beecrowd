final = []
for x in range(10):
    entrada = int(input())
    if entrada < 1:
        entrada = 1
        final.append(entrada)
    else:
        final.append(entrada)
for x in range(10):
    print(f'X[{x}] = {final[x]}')