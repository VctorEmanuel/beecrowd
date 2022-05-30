informado = float(input())
if 0 <= informado <= 25:
    print('Intervalo [0,25]')
elif 25 < informado <= 50:
    print('Intervalo (25,50]')
elif 50 < informado <= 75:
    print('Intervalo (50,75]')
elif 75 < informado <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')