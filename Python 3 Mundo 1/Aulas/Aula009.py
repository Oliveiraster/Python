#Fatiamento

frase = 'Curso em video python'
print(frase[9:13])

frase = 'Curso em video python'
print(frase[9:21])

frase = 'Curso em video python'
print(frase[9:21:2])

frase = 'Curso em video python'
print(frase[:5])

frase = 'Curso em video python'
print(frase[15:])

frase = 'Curso em video python'
print(frase[9::3])

#Análise

frase = 'Curso em video python'
print(len(frase))

frase = 'Curso em video python'
print(frase.count('o'))

frase = 'Curso em video python'
print(frase.count('o', 0, 13))

frase = 'Curso em video python'
print(frase.find('deo'))

frase = 'Curso em video python'
print('curso'in frase )

#Transformação

frase = 'Curso em video python'
print(frase.replace('python', 'Android'))

frase = 'Curso em video python'
print(frase.upper())

frase = 'Curso em video python'
print(frase.lower())

frase = 'Curso em video python'
print(frase.capitalize())

frase = 'Curso em video python'
print(frase.title())

frase = '  Aprenda  Python  '
print(frase.strip())

frase = '  Aprenda Python  '
print(frase.rstrip())

frase = '  Aprenda Python   '
print(frase.lstrip())

#Divisão

frase = 'Curso em video python'
separado = frase.split()
print(frase.split())
#Junção

print('_'.join(separado))




