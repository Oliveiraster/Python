import math
cateto_oposto = float(input('Valor do cateto oposto: '))
cateto_adjacente = float(input('Valor do cateto adjacente'))

resultado = math.hypot( cateto_oposto , cateto_adjacente)

print(resultado)