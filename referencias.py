dicionario1 = {"a" : 1, "b" : 2}
dicionario2 = {"c" : 2, "d" : 3}
# Esta linha não faz uma copia do dicionario
# As duas variaveis dicionario 2 e 3 apontam para a mesma memoria
# ou seja partilham os mesmos dados
dicionario3 = dicionario2
dicionario3["e"]=4
print(dicionario2)
# E se eu quiser fazer uma copia do dicionario
dicionario4 = dicionario3.copy()
dicionario3["pao"] = 3
print(dicionario4)
print(dicionario3)