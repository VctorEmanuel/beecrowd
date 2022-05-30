valores = []
PI = 3.14
while True:    
    entrada = input().split()
    larguraElevador = int(entrada[0])
    comprimentoElevador = int(entrada[1])
    r1, r2 = int(entrada[2]), int(entrada[3])
    
    if larguraElevador == 0 and comprimentoElevador == 0 and r1 == 0 and r2 == 0:
        break
    else: 
        valores.append([larguraElevador, comprimentoElevador, r1, r2])

for x in range(len(valores)):
    [print('S') if valores[x][0] * valores[x][1] >= (valores[x][2]*PI) * (valores[x][3]*PI) else print('N')]