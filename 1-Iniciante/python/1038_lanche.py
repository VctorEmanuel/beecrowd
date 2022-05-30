codigos_preços = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
cod, qtd = input().split(' ')

print(f'Total: R$ {(codigos_preços[int(cod)]*int(qtd)):.2f}')