num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))
num4 = int(input('Digite o 4° número: '))
tupla = (num1, num2, num3, num4)
if 9 in tupla:
    print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na  {tupla.index(3)+1}ª posição.')
if tupla[0] % 2 == 0 or tupla[1] % 2 == 0 or tupla[2] % 2 == 0 or tupla[3] % 2 == 0:
    print('Os valores pares digitados foram ', end='')
    for c in tupla:
        if c % 2 == 0:
            print(c, end='  ')
else:
    print('Nenhum valor PAR foi digitado.')
