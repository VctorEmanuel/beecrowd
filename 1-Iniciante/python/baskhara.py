A = input().split()

delta = (float(A[1])** 2) - (4 *float(A[0])*float(A[2]))
r1 = (-float(A[1])+ (delta ** 0.5)) / (2 *float(A[0]))
r2 = (-float(A[1])- (delta ** 0.5)) / (2 *float(A[0])) 
print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")