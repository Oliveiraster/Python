import datetime

ano = int(input('Qual ano quer analisar ? '))
if ano == 0:
    ano = datetime.date.today().year
#if ano % 4 ==0:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))