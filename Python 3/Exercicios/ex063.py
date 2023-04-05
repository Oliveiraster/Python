termo = int(input('Quantos termos'))
n1 = 0
n2 = 1
resultado = 0
cont = 1
while cont <= termo:
    resultado = n1 + n2
    n2 = n1
    n1 = resultado
    cont += 1
    print('{} '.format(resultado), end='')
print('FIM')
