from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)

print(f'Os números sorteados foram: {n}')
print(f'O mairo numero sorteado foi: {max(n)}')
print(f'O menor número sorteado foi: {min(n)}')
