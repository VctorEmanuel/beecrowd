dias = {'ano': 0, 'mes': 0, 'dia': 0}
A = int(input())
while A != 0:
    if A >= 365:
        A -= 365
        dias['ano'] += 1
    elif A >= 30:
        A -= 30
        dias['mes'] += 1
    else:
        A -= 1
        dias['dia'] += 1
print(f"{dias['ano']} ano(s)\n{dias['mes']} mes(es)\n{dias['dia']} dia(s)")