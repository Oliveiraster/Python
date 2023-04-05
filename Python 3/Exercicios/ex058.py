from time import sleep
from random import randrange
print('Pensei em um número de 0 à 10, tente adivinhas...')
num = int(input('Qual numero estou pensando?!?!  '))
computador = randrange(0, 10)
cont = 1
while num != computador:
    print('Hum... será... ?')
    sleep(1)
    if num > computador:
        num = int(input('É menor que {}.\nTente outra vez: \n'.format(num)))
    else:
        num = int(input('É maior que {}.\nTente outra vez: \n'.format(num)))
    cont += 1
print('Hum... será... ?')
sleep(1)
print('Parabens, eu pensei em {}, você acertou após {} tentativas.'.format(computador, cont))
