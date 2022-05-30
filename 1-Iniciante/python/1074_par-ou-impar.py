vezes = int(input())

for x in range(vezes):
    numero = int(input())
    if numero == 0:
        print('NULL')
    elif numero > 0:
        if numero % 2 == 1:
            print('ODD POSITIVE')
        else:
            print('EVEN POSITIVE')
    else:
        if numero % 2 == 1:
            print('ODD NEGATIVE')
        else:
            print('EVEN NEGATIVE')