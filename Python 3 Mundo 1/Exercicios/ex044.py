valor = float(input('Valor do Produto : \n'))
print('''{ 1 } Pagamento à vista em espécie / Pix: 10% de desconto.
{ 2 } Pagamento no Débito: 5% de Desconto
{ 3 } Pagamento Crédito até 2x Cartão: sem Juros.
      Pagamento Crédito 3x à 10x: 20% Juros''')
opcao = int(input('Selecione a forma de pagamento:\n'))
avista = valor - (valor * 0.1)
debito = valor - (valor * 0.05)
cjuros = valor * 1.2

if opcao == 1:
    print('Com o pagamento à vista/pix vc tem um descont de 10% e o valor pago sera de R${:.2f}.'.format(avista))
elif opcao == 2:
    print('Com o pagamento com cartão de Debito seu Desconto é de 5% e o valor pago será de R${:.2f}.'.format(debito))
elif opcao == 3:
    parcela = int(input('Deseja dividir em quantas vezes ?\n'))
    if parcela <= 2:
        print('''O valor {:.2f}, dividido em {}x, vc pagara {}x de R${:.2f}.
Valor Total R${}.'''.format(valor, parcela, parcela, valor/parcela, valor))
    elif parcela <= 10:
        print('''O valor {:.2f}, dividido em {}x, vc pagara {}x de R${:.2f}.
Valor Total R${}, Juros de 20% aplicado no valor'''.format(valor, parcela, parcela, cjuros/parcela, cjuros))
    elif parcela > 10:
        print('Parcelamos em até 10x\nOPÇÂO INVALIDA.')
elif opcao >= 4:
    print('OPÇÂO INVALIDA!!')
