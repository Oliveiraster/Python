velocar = int(input('Qual a valecidade do veiculo? \n'))
if velocar <= 80:
    print('Continue dirigindo com cuidado!')
else:
    print('MULTADO!! Sua Velocidade foi de {} superior a maxima permitida de 80KM/H.\n'
          'Multa aplicada de {} Reais.'.format(velocar, (velocar - 80)*7))
    print('CUIDADO!!!')
