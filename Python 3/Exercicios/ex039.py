from datetime import date
ano = date.today().year
nome_candidato = str(input('Qual seu nome ? ')).strip()
ano_candidato = int(input('Ano de nascimento?'))
idade_candidato = ano - ano_candidato
print(nome_candidato)
if idade_candidato == 18:
    print('Olá {}, Este é o ano do seu alistamento militar.'.format(nome_candidato))
elif idade_candidato < 18:
    print('Olá {}, Voçê está a {} ano(s) do seu alistamento militar.'.format(nome_candidato, 18 - idade_candidato))
elif idade_candidato > 18:
    print('''Olá {}, Voçê passou {} ano(s) do seu alistamento militar.
    Se diriga até o centro de alistamento mais proximo.'''.format(nome_candidato, idade_candidato - 18))
