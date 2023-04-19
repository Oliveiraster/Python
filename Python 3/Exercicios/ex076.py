tupla = ('Café', 12.50, 'Arroz', 5, 'Cuscuz', 2.15,)
for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:-<30}', end='')
    else:
        print(f' R${tupla[c]:>1.2f}')
