from random import randint
from time import sleep
resultado = []
dados = []
final = []
jogos = {}
print('Valores sorteados: ')
for c in range(1, 5):
    jogos['jogador'] = f'Jogador {c}'
    jogos['resultado'] = randint(1, 6)
    resultado.append(jogos.copy())
for j in resultado:
    print(f'{j["jogador"]} tirou {j["resultado"]} no dado.')
    dados.append(j['resultado'])
    dados.append(j['jogador'])
    final.append(dados[:])
    dados.clear()
    sleep(1)
print('-=' * 30)
finalf = sorted(final, reverse=True)
print('     == RANKING DOS JOGADORES ==')
for i, r in enumerate(finalf):
    print(f'     {i+1}° lugar: {r[1]} com {r[0]} pontos.')
    sleep(0.5)
