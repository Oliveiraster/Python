from random import randrange

print('''Escolha uma opção para jogar: 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual sua escolha? \n'))

lista = ['Pedra', 'Papel', 'Tesoura']
computador = randrange(0, 2)
print('O Computador escolheu {} e você escolheu {}.'.format(lista[computador], lista[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU!!')
    elif jogador == 2:
        print('Computador VENDEU!!')

elif computador == 1:
    if jogador == 0:
        print('Computador VENDEU!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('Jogador VENCEU!!')

elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU!!')
    elif jogador == 1:
        print('Computador VENCEU!!')
    elif jogador == 2:
        print('EMPATE')
