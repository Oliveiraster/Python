tupla = ('aprender', 'programar', 'linguagem', 'python')

for palavra in tupla:
    print(f'\nna palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra.upper()} ', end='')
