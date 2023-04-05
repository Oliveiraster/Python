nome = str(input('Digite seu nome:  ')).strip().lower()


print('A letra A  aparece {} vezes \nA Primeira letra A apareceu na posoção {}\nA última letra A aparece na posição {}'. format(nome.count('a'), nome.find('a')+1, nome.rfind('a')+1))
