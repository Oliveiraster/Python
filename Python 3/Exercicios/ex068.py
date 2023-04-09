from random import randrange
cont = 0
while True:
    opcao = 'R'
    computador = randrange(0, 10)
    jogador = int(input('Digite um Valor: '))
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar ? P/I')).upper()[0]
    if opcao == 'P':
        resultado = (computador + jogador) % 2
        if resultado == 0:
            print('Você Ganhou!!!')
            cont += 1
        else:
            print('Você Perdeu!!')
            break
    if opcao == 'I':
        resultado = (computador + jogador) % 2
        if resultado == 1:
            print('Você Ganhou!!!')
            cont += 1
        else:
            print('Você Perdeu!!!')
            break
print(f'Você teve {cont} VITÓRIA(S), Melhor sorte da proxima.')
