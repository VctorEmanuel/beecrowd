entrada = input().split(' ')
for x in range(len(entrada)): entrada[x] = float(entrada[x])     
entrada = sorted(entrada)
A, B, C = entrada[2], entrada[1], entrada[0]
saida = ''
if A >= B + C:
    saida += 'NAO FORMA TRIANGULO'
else: 
    if A**2 > B**2 + C**2:
        saida += 'TRIANGULO OBTUSANGULO'
    elif A**2 < B**2 + C**2:
        saida += 'TRIANGULO ACUTANGULO'
    else:
        saida += 'TRIANGULO RETANGULO'

    if A == B == C:
        saida += '\nTRIANGULO EQUILATERO'
    elif A == B or B == C or A == C:
        saida += '\nTRIANGULO ISOSCELES'
print(saida)
