animais = {
    'aguia'       : ['vertebrado'  ,      'ave',  'carnivoro'],
    'pomba'       : ['vertebrado'  ,      'ave',    'onivoro'],
    'homem'       : ['vertebrado'  , 'mamifero',    'onivoro'],
    'vaca'        : ['vertebrado'  , 'mamifero',  'herbivoro'],
    'pulga'       : ['invertebrado',   'inseto', 'hematofago'],
    'lagarta'     : ['invertebrado',   'inseto',  'herbivoro'],
    'sanguessuga' : ['invertebrado', 'anelideo', 'hematofago'],
    'minhoca'     : ['invertebrado', 'anelideo',    'onivoro'] 
}
entradas = []
for x in range(3):
    entrada = input()
    entradas.append(entrada)

for x in animais:
    if animais[x] == entradas:
        print(x)
        break