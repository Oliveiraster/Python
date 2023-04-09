cont = num = mult = 1
while True:
    num = int(input('QUer saber a tabuada de qual valor ?'))
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        print(f' {num} X {cont:2} = {num * cont}')
        cont += 1
print('FINALIZADO!!!')
