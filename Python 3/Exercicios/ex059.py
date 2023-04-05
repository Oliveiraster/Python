from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''=-==-==-==-==-==-==-==-==-==-=
[ 1 ] somar
[ 2 ] multiplecar 
[ 3 ] maior
[ 4 ] novo números
[ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Selecione uma opção: '))
    if opcao == 1:
        print('a soma é {}'.format(num1 + num2))
    elif opcao == 2:
        print('A {} multiplicado por {} é {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O número {} é maior que o número {}'.format(num1, num2))
        else:
            print('O número {} é maior que o número {}'.format(num2, num1))
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('\033[32mENCERRANDO...\033[m')
    else:
        print('\033[31mOpção invalida!!\033[m')
sleep(1)
print('\033[35mPrograma Finalizado!!')
