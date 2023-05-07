from datetime import date
ano_atual = date.today().year


def voto(a):
    # As importaçoes feitas dentro da função ajuda na economida de memoria
    parametro = ano_atual - a
    if 18 < parametro <= 60:
        print(f'Com {parametro} anos: VOTO OBRIGATORIO!!!')
    elif parametro <= 18:
        print(f'Com {parametro} anos: NÃO VOTA!!!')
    else:
        print(f'Com {parametro} anos: VOTO OPCIONAL!!!')


voto(int(input('Qual ano vc nasceu ?  ')))
