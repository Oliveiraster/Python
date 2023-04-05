from datetime import date
ano_atual = date.today().year
adulto = 0
jovem = 0
for ano in range(1, 8):
    num = int(input('Qual ano nasceu a {}° Pessoa: '.format(ano)))
    if ano_atual - num < 17:
        jovem += 1
    else:
        adulto += 1
print('Jovens {}, Adultos {}.'.format(jovem, adulto))
