soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um Valor: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Dentro dos {} pares digitados, a soma entre eles Resulta em {}.'.format(cont, soma))
