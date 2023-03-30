peso = float(input('Qual é seu peso ?  (KG) '))
altura = float(input('Qual a sua Altura ? '))
imc = peso / (altura**2)
print('Seu IMC é {:.1f}, Você esta '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do Peso.')
elif imc <= 25:
    print('Peso IDEAL.')
elif imc <= 30:
    print('SOBREPESO.')
elif imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('Obesidade Mórbida.')
