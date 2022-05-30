entrada = input().split()
entrada[0], entrada[1], entrada[2] = list(map(int, entrada))
sort = sorted(entrada)
print(f'{sort[0]}\n{sort[1]}\n{sort[2]}\n\n{entrada[0]}\n{entrada[1]}\n{entrada[2]}')