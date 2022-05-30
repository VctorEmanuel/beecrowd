n = {'par': 0, 'impar': 0, 'positivo': 0, 'negativo': 0}
for x in range(5):
    nn = int(input())
    if nn % 2 == 0:
        n['par'] += 1
    else:
        n['impar'] += 1
    if nn > 0:
        n['positivo'] += 1
    elif nn < 0:
        n['negativo'] += 1
print(f"""{n['par']} valor(es) par(es)
{n['impar']} valor(es) impar(es)
{n['positivo']} valor(es) positivo(s)
{n['negativo']} valor(es) negativo(s)""")