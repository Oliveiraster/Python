lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'EU vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} que está na posição {pos}.')

print('Comi isso tudo oO')
