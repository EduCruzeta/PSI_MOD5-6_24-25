# definir um dicionario utilizamos {chave: valor}

dicionario = {"nome" : "joaquim"}
print(dicionario["nome"])

# Alterar o valor de uma chave
dicionario["nome"] = input("Intruduza um nome: ")
print(dicionario["nome"])

# adicionar novas chaves:valores
dicionario["idade"] = 10
# Chaves e valores podem ser strings ou números
dicionario[10] = "blablabla"
print(dicionario)

# fazer um ciclo para precorrer os pares chaves:valores
chaves = dicionario.keys()      # Devolve uma lista com as chaves
valores = dicionario.values()   # Devolve uma lista com os valores
elementos = dicionario.items()  # Devolve uma lista com os pares chaves:valores
print(chaves,elementos)
for chave in dicionario.keys():
    print(dicionario[chave])
# ciclo precorre os items do dicionario (chave:valore)
for pares in dicionario.items():
    print(f"{pares[0]} : {pares[1]}")

# remover chaves:valores do dicionario
valor = dicionario.pop("idade",None)
print(f"Idade (removida): {valor}")  # Primeira vez devolve 10
print(dicionario)
valor = dicionario.pop("idade",None)
print(f"Idade (removida): {valor}")  # Segunda vez devolve None porque ja não existe
# Remove a cahve indicada entre []
del dicionario["nome"]
print(dicionario)