lista = []
dados = []
maior = menor = cont = 0
pesomaior = []
pesomenor = []
while True:
    dados.append((str(input('Digite o nome: '))))
    dados.append(float(input('Digite o peso: ')))
    lista.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar ? [S/N]')).strip()
    if opcao in 'Nn':
        break
print(f'Ao todo foram cadastrados {len(lista)} pessoas.')
for d in lista:
    if cont == 0:
        maior = d[1]
        dados.append(d[0])
        pesomaior.append(dados[:1])
        dados.clear()

        menor = d[1]
        dados.append(d[0])
        pesomenor.append(dados[:1])
        dados.clear()
    else:
        if d[1] >= maior:
            if d[1] == maior:
                maior = d[1]
                dados.append(d[0])
                pesomaior.append(dados[:])
                dados.clear()
            else:
                maior = d[1]
                pesomaior.clear()
                dados.append(d[0])
                pesomaior.append(dados[:])
                dados.clear()

        if d[1] <= menor:
            if d[1] == menor:
                menor = d[1]
                dados.append(d[0])
                pesomenor.append(dados[:])
                dados.clear()
            else:
                menor = d[1]
                pesomenor.clear()
                dados.append(d[0])
                pesomenor.append(dados[:])
                dados.clear()
    cont += 1
print(f'O maior peso foi de {maior:.1f}KG. Peso de ', end='')
for up in pesomaior:
    print(f'[{up[0]}] ', end='')
print(f'\nO menor peso foi de {menor:.1f}KG. Peso de ', end='')
for up in pesomenor:
    print(f'[{up[0]}] ', end='')
