lista_numeros, n = [], [None, None]
while n[0] != '0' and n[1] != '0':
    n = input().split(' ')
    lista_numeros.append(n)
lista_numeros.pop()
for n in lista_numeros: 
    digit = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}   
    for numeros in range(int(n[0]), int(n[1])+1):
        for numero in str(numeros): digit[int(numero)] += 1              
    for x in range(10):
        if x == 9: print(digit[x])   
        else: print(f"{digit[x]}", end=" ")
            