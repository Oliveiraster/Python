def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem(str(input('Digite um nome: ')))

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
