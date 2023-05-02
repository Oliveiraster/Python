geral = dict()
gol = []
geral['Jogador'] = str(input('Nome do Jogador: '))
qt = int(input(f'Quantas partidas {geral["Jogador"]} jogou ? '))
for j in range(1, qt + 1):
    gol.append(int(input(f'    Quantos gols na {j}º Partida ? ')))
geral['gols'] = gol
somagol = 0
for s in geral['gols']:
    somagol += s
geral['totalgol'] = somagol
print('-=' * 30)
print(geral)
print('-=' * 30)
for t, v in geral.items():
    print(f'O campo {t} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {geral["Jogador"]} Jogou {qt} Partidas.')
for i, c in enumerate(gol):
    print(f'    => Na {i+1}ª partida, fez {c} gols.')
print(f'Foi um total de {geral["totalgol"]} gols.')
