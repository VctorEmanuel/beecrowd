numero = input().split()
A, B, C = float(numero[0]), float(numero[1]), float(numero[2])

if A + B > C and A + C > B and B + C > A:
    print(f'Perimetro = {(A + B + C):.1f}')
else:
    print(f'Area = {(((A + B) * C) / 2):.1f}')