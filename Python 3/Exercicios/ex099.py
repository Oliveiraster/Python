from time import sleep


def analista(*valores):
    print('-=' * 50)
    print(f'Analisando os valores passados ...')
    maior = 0
    for i, c in enumerate(valores):
        print(f'{c} ', end='')
        if {i} == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        sleep(0.5)
    print(f'Foram imformados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


analista(2, 9, 4, 5, 7, 1)
analista(4, 7, 0)
analista(1, 2)
analista(6)
analista()
