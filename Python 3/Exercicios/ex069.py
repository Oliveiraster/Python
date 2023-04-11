opcao = 'S'
contM = contF = maioridade = 0
while True:
    if opcao == 'S':
        print('-' * 20)
        print(f'CADASTRR UMA PESSOA')
        print('-' * 20)
        idade = int(input('Idade: '))
        sexo = 't'
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
        if sexo == 'F' and idade < 20:
            contF += 1
        elif idade >= 18:
            maioridade += 1
            if sexo == 'M':
                contM += 1
        elif sexo == 'M':
            contM += 1
    elif opcao == 'N':
        print('FIM')
        break
    opcao = 't'
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ? [S/N]')).upper()
print(f'''Total de Pessoas com mais de 18:  {maioridade} 
Total de homens cadastrados: {contM}
Total de mulheras com menos de 20 anos: {contF}''')
