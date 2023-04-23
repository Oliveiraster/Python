lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    cont += 1
    while opcao not in 'SN':
        print('Valor invalido')
        opcao = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
lista.sort(reverse=True)
print(f'''Foram digitados {cont} números.
A lista de valores em ordem decrecente é {lista}''')
if 5 in lista:
    print('A lista contem o numero 5.')
else:
    print('A lista nao contem o numero 5.')
