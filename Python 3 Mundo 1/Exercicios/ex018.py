import math
angulo = int(input('Digite o Angulo: '))
cos = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O âgulo de {} tem o SENO de {:.2f}\nO âgulo de {} tem o COSSENO de {:.2f}\nO âgulo de {} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, cos, angulo, tang))