entrada = input().split()
inicio, final = int(entrada[0]), int(entrada[1])
hora = final - inicio
if inicio > final:
	hora += 24
else:
    hora = 24
print(f'O JOGO DUROU {hora} HORA(S)')
