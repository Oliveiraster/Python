'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''c = 0
while c < 10:
    print(c)
    c += 1
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:  '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números Pares e {} números Impares'. format(par, impar))
