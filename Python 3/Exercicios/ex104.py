def leiaint(i):
    situacao = False
    inf = 0
    while True:
        num = str(input(i))
        if num.isnumeric():
            inf = int(num)
            situacao = True
        else:
            print('ERRO, Digita um número válido.')
        if situacao:
            break
    return inf


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
