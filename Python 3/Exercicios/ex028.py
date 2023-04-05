import random
print('====' * 16)
print('Tente adivinhar o Numero que estou pensando, dica: entre 0 e 5.')
print('====' * 16)
usuario = int(input('Qual numero estou pensando? \n').strip())
num = (random.randrange(0, 5))
if num == usuario:
    print('Parabêns, Você Venceu!!!')
else:
    print('O número pensado foi {}.\nTente Novamente!'.format(num))
