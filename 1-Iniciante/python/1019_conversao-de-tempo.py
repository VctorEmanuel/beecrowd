a = int(input())
horas, minutos, segudos = 0, 0, 0
while a > 0:
    if a > 3600:
        horas += 1
        a -= 3600
    elif a > 60:
        minutos += 1
        a -= 60
    else:
        segundos = a
        a = 0

print(f'{horas}:{minutos}:{segundos}')