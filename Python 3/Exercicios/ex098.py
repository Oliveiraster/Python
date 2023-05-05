from time import sleep


def contador(i, f, p):
    print('-=' * 40)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c += p
        print()
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 40)
print('Agora é sua vez de personalizar a contagem!!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
