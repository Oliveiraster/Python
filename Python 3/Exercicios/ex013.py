salario = float(input('Qual Salario atual?\n'))
porcento = float(input('quantos % de aumento?\n'))

porcento_final = porcento / 100 + 1

salario_final = salario * porcento_final

print('Com o aumento de {}% o salaria será de R${:.2f}'.format(porcento, salario_final))