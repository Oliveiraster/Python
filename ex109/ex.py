import moeda9

p = float(input('Digite o preço: R$'))
print(f'''A metade de R${moeda9.moeda(p)} é R${moeda9.metade(p, True)}.
O dobro de R${moeda9.moeda(p)} é R${moeda9.dobro(p, True)}.
Aumentando 10%, temos R${moeda9.aumentar(p, 10, True)}
Resuzindo 13%, temos {moeda9.diminuir(p, 13, True)}''')
