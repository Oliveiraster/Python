produto = float(input('Qual valor do produto que você deseja aplicar o desconto de 5% ?\n'))

vdesconto = produto * 0.05
desctotal = produto - vdesconto

print('Com a aplicação de 5% de desconto em cima do valor {} o valor final sera de {:.2f}.'.format(produto, desctotal))