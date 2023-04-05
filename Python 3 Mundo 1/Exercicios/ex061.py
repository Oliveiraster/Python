inicio = int(input('Primeiro Termo: '))
razao = int(input('Razao:  '))
termo = int(input('quantos termos a + vc quer ?'))
cont = 1
total = 0
while cont <= termo:
    print('{} > '.format(inicio), end='')
    inicio += razao
    cont += 1
    total += 1
print('FIM')
