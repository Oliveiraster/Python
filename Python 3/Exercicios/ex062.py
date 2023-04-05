inicio = int(input('Primeiro Termo: '))
razao = int(input('Razao:  '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(inicio), end='')
        inicio += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer adicionar ? '))

print('As Progressôes foram no total de {}'.format(total))
