def calculodearea(a, b):
    x = a * b
    print(f'A área de um terreno{a}x{b} é de {x:.1f}m²')


print('   Controle de Terrenos')
print(30 * '_')
Comp = float(input('LARGURA  (m): '))
Larg = float(input('COMPRIMENTO (m): '))
calculodearea(Comp, Larg)
