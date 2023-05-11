import moeda8

p = float(input('Digite o preço: R$'))
print(f'''A metade de R${moeda8.moeda(p)} é R${moeda8.moeda(moeda8.metade(p))}.
O dobro de R${moeda8.moeda(p)} é R${moeda8.moeda(moeda8.dobro(p))}.
Aumentando 10%, temos R${moeda8.moeda(moeda8.aumentar(p, 10))}.''')
