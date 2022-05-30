entrada = input().split()
hora_i, min_i, hora_f, min_f = list(map(int, entrada))
hora, minuto = hora_f - hora_i, min_f - min_i 
if hora_i == hora_f:     
    if min_i == min_f:
        hora = 24 
        minuto = 0 
    elif min_i > min_f:
        hora = 24
        hora -= 1
        minuto += 60
    else: pass   
elif hora_i > hora_f: 
    hora += 24
    if min_i > min_f:
        minuto += 60
        hora -= 1  
    else: pass
else: 
    if min_i >= min_f:
        hora -= 1
        minuto += 60
    else: pass

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')