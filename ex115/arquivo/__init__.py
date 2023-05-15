def doctrue(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def newarquivo(msg):
    try:
        arq = open(msg, 'wt+')
        arq.close()
    except:
        print('Houve um Erro na criação do arquivo')
    else:
        print(f'Arquivo{msg} criado com sucesso!')


def lerarquivo(msg):
    from ex115.biblioteca import cabecalho
    try:
        arq = open(msg, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arq.close()


def cadastrar(doc, nome='Desconhecido', idade='none'):
    try:
        a = open(doc, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!!')
        else:
            print(f'{nome} cadastrado com sucesso!')
            a.close()
