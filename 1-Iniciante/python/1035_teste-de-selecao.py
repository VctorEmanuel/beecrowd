# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, 
# e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A 
# for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

n = input().split()
A, B, C, D = int(n[0]), int(n[1]), int(n[2]), int(n[3]),  
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')