a = int(input())
b = int(input())
if b < 0:
    b = b - b*2
print(f'{a / b} {a % b}')