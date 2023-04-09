from time import sleep
r = 'S'
maior = menor = cont = total = 0
while r == 'S':
    num = int(input('Digite um Valor: '))
    total += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer digitar outro valor? [S/N] :')).upper()[0]
    if r not in 'NS':
        print('\033[31m OPÇÂO INVALIDA!!\033[m')
        sleep(1)
        r = str(input('Quer digitar outro valor? [S/N] :')).upper()[0]
media = total / cont
print('''A média dos {} números digitados é {}.
O Menor é {} e o Maior é {}. '''.format(cont, media, menor, maior))
