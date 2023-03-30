from datetime import date
ano = date.today().year
atleta = int(input('Ano de Nascimento:  '))
idade_corte = ano - atleta

if idade_corte > 25:
    print('O atleta tem {} anos. \nCategoria: MASTER!!'.format(idade_corte))
elif idade_corte > 19:
    print('O atleta tem {} anos. \nCategoria: SENIOR!!'.format(idade_corte))
elif idade_corte > 14:
    print('O atleta tem {} anos. \nCategoria: JUNIOR!!'.format(idade_corte))
elif idade_corte > 9:
    print('O atleta tem {} anos. \nCategoria: INFANTIL!!'.format(idade_corte))
else:
    print('O atleta tem {} anos. \nCategoria: MIRIN!!'.format(idade_corte))
