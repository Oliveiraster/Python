km = float(input('Quantos quilometros será sua viagem ? '))
km1 = 200
if km <= km1:
    print('O valor da viagem será de R${:.2f}.'.format(km * 0.50))
else:
    print('O valor da viagem será de R${:.2f}.'.format(km * 0.45))
