entrada = input().split()
A, B, C = float(entrada[0]), float(entrada[1]), float(entrada[2])

print(f"""TRIANGULO: {A*C/2:.3f}
CIRCULO: {3.14159*C**2:.3f}
TRAPEZIO: {(A+B)*C/2:.3f}
QUADRADO: {B**2:.3f}
RETANGULO: {A*B:.3f}""")

# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.