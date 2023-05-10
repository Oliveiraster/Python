def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: Um ou mais notas dos alunos (aceita várias)
        :param sit: Valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionario com várias situaçoes e a situação da turma.
        """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
