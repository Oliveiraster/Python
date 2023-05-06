from random import randint
geral = []


def sorteio():
    print(f'Sorteando 5 valores da Lista : ', end='')
    for c in range(0, 5):
        num = randint(0, 11)
        geral.append(num)
        print(f'{num} ', end='')
    print('PRONTO!!')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}.')


sorteio()
somapar(geral)
