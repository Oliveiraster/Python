listas = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        listas[0].append(num)
    else:
        listas[1].append(num)

print(f'Lista PAR {sorted(listas[0])}')
print(f'Lista IMPAR {sorted(listas[1])}')
