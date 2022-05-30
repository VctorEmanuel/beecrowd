numeros = []
ns, positivos = 0, 0
for x in range(6):
    numeros.append(float(input()))
for numero in numeros:
    if numero > 0: 
        ns += 1
        positivos += numero
print(f'{ns} valores positivos\n{(positivos/ns):.1f}')