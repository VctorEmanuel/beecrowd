entrada = input().split()
a, b = int(entrada[0]), int(entrada[1])
print('Sao Multiplos') if b % a == 0 or a % b == 0 else print('Não são múltiplos')