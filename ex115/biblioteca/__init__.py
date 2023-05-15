def leiaint(i):
    while True:
        try:
            n = int(input(i))
        except(ValueError, TypeError):
            print('\033[31mErro!! digite um númeto inteiro válido! \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '=' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(me):
    cabecalho('MENU PRINCIPAL')
    for i, m in enumerate(me):
        print(f'\033[36m{i+1} <> \033[32m{m} \033[m')
    print(linha())
    opcao = leiaint(f'\033[34mSua opção: \033[m')
    return opcao
