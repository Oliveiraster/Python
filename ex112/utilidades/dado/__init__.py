def leiadinheirp(msg):
    v = False
    while not v:
        ent = str(input(msg).replace(',', '.').strip())
        if ent.isalpha() or ent.strip() == '' or not ent.isnumeric():
            print(f'Erro: \"{ent}\" é um preço inválido!')
        else:
            v = True
            return float(ent)

