altparede = float(input('Qual a medida em metros da altura da parede?\n'))
largparede = float(input('Qual a medida em metros da largura da parede? \n'))

mquadrado = altparede * largparede

ltinta = mquadrado / 2

print('Para executar a pintura da parede quem tem um total de {} m2,\nserá necessario usar {} litros de tinta!'.format(mquadrado, ltinta))