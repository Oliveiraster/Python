def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Um ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias situaçoes e a situação da turma.
    """

    res = dict()
    res['total'] = len(nota)
    maior = menor = soma = 0
    for i, n in enumerate(nota):
        soma += n
        if i == 0:
            maior = n
            menor = n
        else:
            if maior < n:
                maior = n
            if menor > n:
                menor = n
    media = soma / len(nota)
    res['maior'] = maior
    res['menor'] = menor
    res['média'] = media
    if sit:
        if media < 5:
            res['situação'] = 'Ruim'
        elif media >= 7:
            res['situação'] = 'Boa'
        elif 5 <= media < 7:
            res['situação'] = 'Razoavel'
    return res


resp = notas(2.5, 1.5, 5.5, 5)
print(resp)
help(notas)
