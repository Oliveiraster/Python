num = list()
while True:
    num1 = (int(input('Digite um Valor: ')))
    if num1 not in num:
        num.append(num1)
        print('Valor adicionado com sucesso.')
    else:
        print('Numero ja existente, nao vou adicinoar...')
    opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    while opcao not in 'SN':
        print('Valor invalido')
        opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Você digitou os valors {sorted(num)}')
