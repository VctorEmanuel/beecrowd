x = int(input())
y = int(input())
aux, soma = 0, 0
if x < y:
    aux = x
    x = y
    y = aux
while x > y+1: 
    x-=1
    if x % 2 == 1:
        soma += x
print(soma)
