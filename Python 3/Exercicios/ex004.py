valor = input('Digite algo: ')
print('O tipo primitivo desse valorusu é',type(valor))
print('Só tem espaço? ', valor.isspace())
print('É um número? ', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Esta em maiúsculas?', valor.isupper())
print('Esta em minusculas?', valor.islower())
print('Esta captalizada?', valor.istitle())