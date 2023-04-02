primeiro = int(input('Inicio'))
razao = int(input('Digite a razão: '))
pa = primeiro + (10-1) * razao
pa += 1

for c in range(primeiro, pa, razao):
    print('{}'.format(c), end=' ')

# Sulução guanabara

primeirog = int(input('\nPrimeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeirog + (10 - 1) * razão
for cg in range(primeirog, décimo + razão, razão):
    print('{}'.format(cg), end='¬ ')
print('ACABOU')
