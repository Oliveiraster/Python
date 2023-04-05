'''nome = ''
while nome != 'RAPHAEL':
    nome = str(input('Digite um nome')).upper()
    if nome == 'RAPHAEL':
        print('\033[42mACERTOU!!')
    else:
        print('\033[31mINVALIDO\033[m')'''

sexo = str(input('Informe seu Sexo: M/F: ')).strip().upper()[0]
while sexo not in 'MF ':
    print('Valor invalido')
    sexo = str(input('Informe corretamente Sexo: M/F: ')).strip().upper()[0]
print('Sexo valido registrado.')
