notas = []
dados = []
while True:
    dados.append(str(input('Nome do aluno: ')))
    dados.append(float(input('1º nota: ')))
    dados.append(float(input('2º nota: ')))
    notas.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'No.  NOME           MÉDIA')
print('-' * 30)
for i, c in enumerate(notas):
    print(f'{i:<2}   {c[0]:<10}  {(c[1] + c[2]) / 2:>8}')
print('-' * 30)
while True:
    opcao2 = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
    if opcao2 == 999:
        break
    print(f'Notas de {notas[opcao2][0]} são {notas[opcao2][1:]}')
print('Finalizado')
print('<<<< VOLTE SEMPRE >>>>')
