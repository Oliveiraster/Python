try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividi um número por Zero!!')
except KeyboardInterrupt:
    print('o Usuario preferiu não informar os dados!')
else:
    print(f'Resultado é {r:.1f}')
finally:
    print('Volte sempre!! Muito Obrigado!')
