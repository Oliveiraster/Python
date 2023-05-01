from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - ano
cadastro['carteira'] = int(input('N° Carteira de Trabalho (0 não tem): '))
if cadastro['carteira'] == 0:
    print(f'''- nome tem o valor {cadastro["nome"]}
- idade tem valor {cadastro['idade']}
- ctps tem o valor 0 ''')
else:
    cadastro['contrato'] = int(input('Ano de contratação: '))
    cadastro['salario'] = str(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contrato'] + 35) - date.today().year)
    print(f'''- nome tem o valor {cadastro["nome"]}
- idade tem o valor {cadastro["idade"]}
- ctps tem o valor {cadastro["carteira"]}
- contratação tem valor {cadastro["contrato"]}
- salário tem valor {cadastro['salario']}
- aposentadoria tem valor {cadastro['aposentadoria']}''')
