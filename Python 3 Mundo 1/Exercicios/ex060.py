'''num = int(input(' Digite:  '))
cont = 1
valor = 1
while cont <= num:
    valor *= cont
    cont += 1
print(valor)
print(cont)'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
