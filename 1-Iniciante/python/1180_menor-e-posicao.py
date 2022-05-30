# n = int(input())
# x = list(map(int, input().split()))

# print('Menor valor:', min(x))
# print('Posicao:', x.index(min(x)))

n=int(input())
x=[]
a=list(map(int,input().split()))
for i in range (n):
    x.insert(i,a[i])
print("Menor valor: %d" %(min(x)))
for i in range(n):
    if x[i]==min(x):
        pos=i
print("Posicao: %d" %pos)