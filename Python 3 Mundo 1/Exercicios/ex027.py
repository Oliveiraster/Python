nome = str(input('Digite sua frase:  '))
primeira_palavra = nome.split()
segunda_palavra = primeira_palavra[::-1]

print('A Primeira palavra digitada foi {}. \nA última palavra digitada foi {}.'.format(primeira_palavra[0], segunda_palavra[0]))

# print((primeira_palavra[len(primeira_palavra)-1])) << Solução aplicada do Guanabara.