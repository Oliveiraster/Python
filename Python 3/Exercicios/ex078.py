valores = list()
menor = maior = cont = 0
for c in range(0, 6):
    valores.append(int(input(f'Digite o valor na posição {c}:  ')))
print(valores)
for v in valores:
    if cont == 1:
        maior = v
        menor = v
    else:
        if v <= menor:
            menor = v
        if v >= maior:
            maior = v
    cont += 1
print(f'O maior valor foi {maior} e se encontra na posição ', end='')
for c, t in enumerate(valores):
    if t == maior:
        print(f'{c}...', end='')
print(f'\nO menor Valor foi {menor} e se encontra na posição ', end='')
for c, t in enumerate(valores):
    if t == menor:
        print(f'{c}...', end='')
