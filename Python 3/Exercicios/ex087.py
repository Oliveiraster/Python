matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = (int(input(f'Digite um valor para [{linha},{coluna}]:  ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
somapar = 0
for n in matriz:
    for s in n:
        if s % 2 == 0:
            somapar += s
print(f'A soma dos valores pares dentro da matriz é {somapar}.')
print(f'A soma do valor os itens da terceira coluna é {matriz[0][2] + matriz[1][2] +matriz[2][2]}')
print(f'o Maior Valor da segunda linha é {max(matriz[1])}')
