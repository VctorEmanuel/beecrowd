informado = input()

if ',' in informado: 
    informado = informado.replace(',', '.')
informado = float(informado)

notas = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0}
moedas = {'1': 0, '0.50': 0, '0.25': 0, '0.10': 0, '0.05': 0, '0.01': 0}	

while informado > 0.00:
    informado = round(informado, 2)
    if informado >= 100.00:
        notas['100'] += 1
        informado -= 100.00
    elif informado >= 50.00:
        notas['50'] += 1
        informado -= 50.00
    elif informado >= 20.00:
        notas['20'] += 1
        informado -= 20.00
    elif informado >= 10.00:
        notas['10'] += 1
        informado -= 10.00
    elif informado >= 5.00:
        notas['5'] += 1
        informado -= 5.00
    elif informado >= 2.00:
        notas['2'] += 1
        informado -= 2.00
    elif informado >= 1.00:
        moedas['1'] += 1
        informado -= 1.00
    elif informado >= 0.50:
        moedas['0.50'] += 1
        informado -= 0.50
    elif informado >= 0.25:
        moedas['0.25'] += 1
        informado -= 0.25
    elif informado >= 0.10:
        moedas['0.10'] += 1
        informado -= 0.10
    elif informado >= 0.05:
        moedas['0.05'] += 1
        informado -= 0.05
    else:
        moedas['0.01'] += 1
        informado -= 0.01
    
print(f'''NOTAS:
{notas['100']} nota(s) de R$ 100.00
{notas['50']} nota(s) de R$ 50.00
{notas['20']} nota(s) de R$ 20.00
{notas['10']} nota(s) de R$ 10.00
{notas['5']} nota(s) de R$ 5.00
{notas['2']} nota(s) de R$ 2.00
MOEDAS:
{moedas['1']} moeda(s) de R$ 1.00
{moedas['0.50']} moeda(s) de R$ 0.50
{moedas['0.25']} moeda(s) de R$ 0.25
{moedas['0.10']} moeda(s) de R$ 0.10
{moedas['0.05']} moeda(s) de R$ 0.05
{moedas['0.01']} moeda(s) de R$ 0.01''')

