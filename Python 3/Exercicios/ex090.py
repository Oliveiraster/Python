avaliacao = dict()
avaliacao['nome'] = str(input('Nome: '))
avaliacao['media'] = float(input(f'Média do {avaliacao["nome"]}: '))
print(f'''- nome é igual a {avaliacao["nome"]}
- média é igual a {avaliacao["media"]}''')
if avaliacao['media'] >= 7:
    print('- situação é igual a APROVADO!!')
else:
    print('- situação é igual a RECUPERAÇÂO!!')

# Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
