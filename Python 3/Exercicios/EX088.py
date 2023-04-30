from random import randint
lista = []
dado = []
cont = 1
stop = int(input(f'Quantos jogos ? '))
while True:
    for numl in range(0, 6):
        num = (randint(0, 61))
        if numl not in lista:
            dado.append(num)
    lista.append(dado[:])
    dado.clear()
    if cont == stop:
        break
    cont += 1
contador = 0
for i in lista:
    print(f'{contador + 1}º jogo:  {sorted(i)}')
    contador += 1
