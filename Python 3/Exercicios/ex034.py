salario = float(input('Qual o salário atual  ?'))
valor_corte = 1250.00


if salario >= valor_corte:
    print('Você ganhara 10% de aumento, seu salário passa a ser R${}'.format(salario*1.1))
else:
    print('Você ganhara 15% de aumento, seu salário passa a ser R${}'.format(salario*1.15))
