'''frase = str(input('Digite aqui:  \n')).strip()
clean = frase.replace(' ', '').upper()
invert = clean[::-1]
print(clean)
print(invert)
if clean == invert:
    print('É um Palíndromo!')
else:
    print('Não é um Palíndromo!')'''
# Solução com for

frase = str(input('Digite aqui:  \n')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo1')

