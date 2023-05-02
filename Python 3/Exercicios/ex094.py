pessoas = []
dados = {}
somaid = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F]')).upper()
    while dados['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F]')).upper()
    dados['idade'] = int(input('Idade: '))
    somaid += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    opcao = str(input('Quer continuar ? [S/N]')).upper()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ? [S/N]')).upper()
    if opcao in 'N':
        break
media = somaid / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) a média de idade do Grupo é {media:.1f}.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for c in pessoas:
    if c['sexo'] in 'F':
        print(c['nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for i in pessoas:
    if i['idade'] > media:
        print(f'   nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}; ')
print('<< FINALIZADO >>')
