print('-' * 30)
print('{:^30}'.format('Banco PH'))
print('-' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if total > 0:
            print(f'Total de {cont} cedulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break
print('FIM')
