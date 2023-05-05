def escreva(msg):
    m = len(msg) + 1
    print('~' * m)
    print(msg)
    print('~' * m)


b = str(input('Digite a mesagem: '))
escreva(b)
