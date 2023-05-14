while True:
    ok1 = ok2 = False
    while True:
        try:
            ni = int(input('Digite um número Inteiro:  '))
        except Exception as erro:
            print('\033[31mErro! Por favor digite um numero inteiro válido!\033[m')
        else:
            ok1 = True
            break
    while True:
        try:
            nf = float(input('Digite um Valor Real:  '))
        except Exception as erro:
            print('\033[31mErro! Por favor digite um numero Real válido!\033[m')
        else:
            ok2 = True
            break
    if ok1 is True and ok2 is True:
        break

print(f'O valor inteiro digitado foi {ni} e o real foi {nf}.')
