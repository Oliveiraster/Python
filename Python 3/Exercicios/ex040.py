nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Sua Média foi {:.1f} voçê está APROVADO!!!'.format(media))
elif media >= 5:
    print('Sua Média foi {:.1f} voçê está RECUPERAÇÂO!!'.format(media))
elif media < 5:
    print('Sua Média foi {:.1f} voçê está REPROVADO!!'.format(media))
