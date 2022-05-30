import math

entrada = input().split()
n = int(entrada[1])
r = int(entrada[0])
pi = 3.1415
v = (4 / 3) * (pi * r ** 3) 
print(math.floor(n/v))