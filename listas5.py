# conversão de listas em dicionarios e o inverso
meu_dicionario = {"nome":"joaquim","idade":15,"morada":"viseu"}

minha_lista = list(meu_dicionario.items())

print(minha_lista)

# converter 2 listas em dicionario

chaves = ["nome","idade","morada"]
valores = ["joaquim",16,"Viseu"]

dicionario = dict(zip(chaves,valores))

print(dicionario)