n = int(input('Digite um Numero inteiro: '))
print('''Escolha uma base para conversão: 
{ 1 } Converte para HEXADECIMAL
{ 2 } Converte para OCTAL
{ 3 } Converte para BINÁRIO''')
funcao = int(input('Selecione uma opção: '))
if funcao == 1:
    print('O Valor de {} convertido para Hexadecimal é {}.'.format(n, hex(n)[2:]))
elif funcao == 2:
    print('O Valor de {} convertido para Octal é {}.'.format(n, oct(n)[2:]))
elif funcao == 3:
    print('O Valor de {} convertido para Binário é {}.'.format(n, bin(n)))
else:
    print('OPÇÂO INVALIDA!!\nDigite uma opção valida.')