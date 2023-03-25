
a = float(input('Insita o primeiro comprimento: '))
b = float(input('Insita o segundo comprimento: '))
c = float(input('Insita o terceiro comprimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Com essas medidas você consegue formar um triâgulo. ')
else:
    print('Com essas medidas você não consegue formar um triângulo. ')
