lista = []
geral = dict()
gol = []
while True:
    geral['Jogador'] = str(input('Nome do Jogador: '))
    qt = int(input(f'Quantas partidas {geral["Jogador"]} jogou ? '))
    for j in range(1, qt + 1):
        gol.append(int(input(f'    Quantos gols na {j}º Partida ? ')))
    geral['gols'] = gol[:]
    somagol = 0
    for s in geral['gols']:
        somagol += s
    geral['totalgol'] = somagol
    lista.append(geral.copy())
    gol.clear()
    geral.clear()
    while True:
        opcao = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Digite apenas N ou S.')
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'{"Cod":<2} {"NOME":<14} {"gols":<10} {"Total":>8}')
print('-' * 60)
for i, l in enumerate(lista):
    print(f'{i:>3} ', end='')
    for c in l.values():
        print(f'{str(c): <15}', end='')
    print()
print('-' * 60)
while True:
    num = int(input('Mostrar dados de qual jogador ? (999 para parar)'))
    if num > len(lista) - 1:
        print(f'ERRO! não existe valor {num} na lista.')
    else:
        print(f'-- LEVANTAMENDO DO JOGADOR  {lista[num]["Jogador"]}: ')
        for i, c in enumerate(lista[num]['gols']):
            print(f'    => Na {i+1}ª partida, fez {c} gols.')
        print(f'Foi um total de {lista[num]["totalgol"]} gols.')
    if num == 999:
        break
    