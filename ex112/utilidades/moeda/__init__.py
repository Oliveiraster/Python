def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, din='R$'):
    return f'{din}{preco:>.2f}'.replace('.', ',')


def resumo (preco=0, taxaA=10, taxaD=5):
    print('=' * 30)
    print('RESUMO DO VALOR')
    print('=' * 30)
    print(f'''Preço analisado: \t{moeda(preco)}
Dobro do preço: \t{dobro(preco, True)}
Metade do preço: \t{metade(preco, True)}
{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}
{taxaD}% de redução: \t{diminuir(preco, taxaD, True)}''')
    print('=' * 30)
