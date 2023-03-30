num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O Numero {} é Maior que o {}.'.format(num1, num2))
elif num1 < num2:
    print('O Número {} é Menor que o {}'.format(num1, num2))
elif num1 == num2:
    print('Os números tem o mesmo Valor, ambos são iguais.')
