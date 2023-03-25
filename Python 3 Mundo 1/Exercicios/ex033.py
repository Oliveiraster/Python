num1 = float(input('Digite o primeiro Número: '))
num2 = float(input('Digite o segundo Número: '))
num3 = float(input('Digite o Terceiro Número: '))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('o menor valor é {}.'.format(menor))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('o menor valor é {}.'.format(maior))
