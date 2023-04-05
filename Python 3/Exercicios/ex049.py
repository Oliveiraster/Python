num = int(input('Qual valor deseja multiplicar? '))
mult = 0
for c in range(1, 11):
    mult += 1
    print('{} X {} = {}'.format(num, mult, num * mult))

# Solução do Guanabara

numg = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(numg, c, num*c))
