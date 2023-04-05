Dias_alugado = int(input('Quantos dias alugado?\n'))
km_rodados = float(input('Quantos KModados?\n'))

Vdia = Dias_alugado * 60
Vkm = km_rodados * 0.15

total = Vdia + Vkm
print('O total a pagar é de Rw${:.2f}'.format(total))