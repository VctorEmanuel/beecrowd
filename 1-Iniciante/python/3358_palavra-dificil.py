
vogais = ['a', 'e', 'i', 'o', 'u']
nomes = {}
saida = ''
N = int(input())
for x in range(N):     
    nome = input('')
    nomes[nome] = 0 
    for y in range(len(nome)):
        if y + 2 != len(nome):
            if (nome[y] not in vogais) and (nome[y+1] not in vogais) and (nome[y+2] not in vogais):  
                nomes[nome] = 1
        else:
            break  
for nome in nomes:   
    if nomes.get(nome) == 1:
        saida = saida + f'{nome} nao eh facil\n'
    else:
        saida = saida + f'{nome} eh facil\n'
print(saida)