lista1 = ('Zero', 'um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
lista2 = ('Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenovo', 'Vinte')
listafull = lista1 + lista2

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 20 >= num >= 0:
        print(f'Você Digitou {listafull[num]}')
        break
