lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'Avai', 'Juventude')
print(' ' * 20)
print(f'Lista de times do Brasileirão:\n{lista}')
print(' ' * 20)
print(f'Os 5 primeiros são:\n{lista[:6]}')
print(' ' * 20)
print(f'Os 4 últimos são:\n{lista[16:]}')
print(' ' * 20)
print(f'Times em Ordem alfabética:\n{sorted(lista)}')
print(' ' * 20)
print(f'O Santos está na {lista.index("Santos")+1}ª posição.')
