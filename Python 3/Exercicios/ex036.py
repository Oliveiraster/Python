valor_imovel = float(input('Qual o Valor do imovel?  '))
salario = float(input('Qual o salario do comprador ? '))
n_prestacao = int(input('Em quantos anos pretende quitar o valor ? '))

prestacao = valor_imovel / (n_prestacao*12)
valor_corte = salario * 0.3

if prestacao <= valor_corte:
    print('As parcelas firacam no valro de {:.2f}, é menor que 30% do valor do salario.\nEMPRESTIMO APROVADO!! '.format(prestacao))

elif prestacao > valor_corte:
    print('As parcelas ficaram no valor de {:.2f}, é maior que 30% do valor do salario.\nEMPRESTIMO NEGADO!!'.format(prestacao))
