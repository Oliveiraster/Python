listaimp = []
listapar = []
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimp.append(num)
    opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    while opcao not in 'SN':
        print('Valor invalido')
        opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'''a lista completa é {sorted(listapar + listaimp)}
A lista de números Pares é {listapar}
Alista de números impares é {listaimp}''')
