notas = input().split()
for x in range(4):
    notas[x] = float(notas[x]) 
media = (notas[0]*2+notas[1]*3+notas[2]*4+notas[3]*1)/(2+3+4+1)
saida = f'Media: {round(media, 1)}'
if media < 5:
    saida += '\nAluno reprovado.'
elif media >= 7:
    saida += '\nAluno aprovado.'
elif 5 <= media < 7:
    saida += '\nAluno em exame.'
    exame = float(input())
    saida += f'\nNota do exame: {exame}'
    mediaf = (media+exame)/2
    if mediaf >= 5:
        saida += '\nAluno aprovado.'
    else: 
        saida += '\nAluno reprovado.'
    saida += f'\nMedia final: {round(mediaf, 1)}'
print(saida)
