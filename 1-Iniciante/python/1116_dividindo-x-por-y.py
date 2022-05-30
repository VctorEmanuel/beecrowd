N = int(input())
for x in range(N):
    a = input().split()
    print("divisao impossivel" if int(a[1]) == 0 else int(a[0])/int(a[1]))