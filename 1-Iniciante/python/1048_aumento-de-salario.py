ifs = [[0.0, 400.0, 15], [400.01, 800.00, 12], [800.01, 1200.00, 10], [1200.01, 2000.00, 7]]

salario = float(input())

if salario > 2000.00:
    novosala, per = salario * (4/100), 4    
else:   
    for a, b, perc in ifs: 
        if a <= salario <= b:
            novosala, per = salario * (perc/100), perc
print(f"""Novo salario: {(novosala+salario):.2f}
Reajuste ganho: {(novosala):.2f}
Em percentual: {per} %""")