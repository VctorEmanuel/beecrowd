multiplos = {'1': 0, '2': 0, '3': 0, '4': 0}
for x in range(int(input())):
    n = int(input())
    for multi in range(2, 6):
        if n % multi == 0:
            multiplos[str(multi)] += 1
