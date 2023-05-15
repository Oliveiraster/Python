from ex115.arquivo import *
from ex115.biblioteca import *
from time import sleep


doc = 'listadecadastro.txt'
if doctrue(doc):
    print('Arquivo encontrado!!')
else:
    newarquivo(doc)
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        lerarquivo(doc)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(doc, nome, idade)
    elif resposta == 3:
        cabecalho('Finalizando ... Até logo!')
        break
    else:
        print('\033[31mERRO!! Digite uma opção válida!\033[m')
    sleep(1.5)
