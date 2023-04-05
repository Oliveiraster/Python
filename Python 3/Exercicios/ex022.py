nome = input('Digite seu nome completo:\n')
fatia = nome.split()
semespaco = nome.replace(' ', '')

print('Nome em maiúscula: ', nome.upper())

print('Nome em minúscula: ', nome.lower())
print('Quantidade de caracteres completo: ', len(nome))
print('Quantidade de caracteres sem espaço: ', len(semespaco))

print('Este é seu Primeiro nome: ', fatia[0])
print('Seu primeiro nome possue ', len(fatia[0]), 'caracteres')
