print('''
eleição 2021

[1] - nulo
[2] - lula
[3] - bolsonaro
[111] - sair
''')

voto = nulo = bolsonaro = lula = 0
cont = 1

while voto != 111:
    voto = int(input('proximo eleitor, qual seu voto [111 - para encerrar as votações]: '))
    cont += 1 
    if voto == 1:
        nulo += 1
        print('voto nulo registrado com sucesso')
    if voto == 2:
        lula += 1
        print('voto em lula registrado com sucesso')
    if voto == 3:
        bolsonaro += 1
        print('voto em bolsonaro registrado com sucesso')
    if voto !=1 and voto != 2 and voto != 3:
        print('opção invalida tente novamente')
        cont -= 1


maior = nulo
menor = nulo

if lula > maior:
    maior = lula
if bolsonaro > maior:
    maior = bolsonaro

print('''
FIM DAS ELEÇÕES 2022
HOUVERAM {} ELEITORES PRESENTES
os resultados foram nulo: {} - lula: {} - bolsonaro: {} 
vencedor = {}'''.format(cont - 1, nulo, lula, bolsonaro, maior))
