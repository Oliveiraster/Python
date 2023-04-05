n1 = int(input('Digite um valor: '))
n2 = 0
resultado = 0
cont = 0
while n2 != 999:
    resultado = n1 + n2
    n1 = resultado
    cont += 1
    n2 = int(input('Digite um valor: '))
print('Foram digitados {} números e o resultado da soma foi {}'.format(cont, resultado))
