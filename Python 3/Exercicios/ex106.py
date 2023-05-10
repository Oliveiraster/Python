c = (
    '\033[m',
    '\033[0;30;41m',
    '\033[0;30;42m',
    '\033[0;30;43m',
    '\033[0;30;44m',
    '\033[0;30;45m',
    '\033[7;39m'
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~' * len(msg))
    print(f'{msg}')
    print('~' * len(msg))
    print(c[0], end='')


while True:
    titulo('Sistema de ajuda Pyhelp', 2)
    comando = str(input('Função ou Bilioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!!', 1)
