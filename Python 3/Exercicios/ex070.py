cont = vtotal = menor_valor = start = 0
nproduto = ' '
print('-'*25)
print('     lOJÃO DO PREÇO')
print('-'*25)
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    vtotal += preco
    start += 1
    if preco >= 1000:
        cont += 1
    if start == 1:
        menor_valor = preco
        nproduto = produto
    else:
        if preco < menor_valor:
            menor_valor = preco
            nproduto = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar?  [S/N]')).strip().upper()
    if opcao == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'''O total da compra foi R${vtotal:.2f}
Temos {cont} produtos custando mais de R$1000.00
O produto mais barato é {nproduto} custando {menor_valor:.2f}.''')
