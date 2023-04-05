contsexof = 0
contidade = 0
mediaidade = contidade / 2
maior = 0
nomemaior = ''
for cadastro in range(1, 5):
    print('----- {}ª PESSOA -----'.format(cadastro))
    nome = str(input('NOME: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    contidade += idade
    if sexo == 'F' and idade < 20:
        contsexof += 1
    mediaidade = contidade / cadastro
    if cadastro == nome and sexo == 'M':
        maior = idade
    if idade > maior and sexo == 'M':
        maior = idade
        nomemaior = nome


print('A media de idade do grupo é {} .'.format(mediaidade))
print('O homem mais velho tem {} e seu nome é {} '. format(maior, nomemaior))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contsexof))
