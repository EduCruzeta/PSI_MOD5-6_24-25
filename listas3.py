# juntar 2 listas
meus_carros = ["ford","bmw"]
teus_carros = ["mercedes","vw"]

# junta as listas numa lista nova sem alterar as iniciais
nossos_carros = meus_carros + teus_carros
print(nossos_carros)

# junta na lista meus_carros todos os elementos da lista teus_carros (não altera a 2/teus_carros)
meus_carros.extend(teus_carros)
print(meus_carros,teus_carros)