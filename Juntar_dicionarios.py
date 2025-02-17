dicionario1={"a" : 1 , "b" : 2 , "c" : 3}
dicionario2 = {"c" : 4 , "d" : 5}

# juntar dois dicionarios
dicionario1.update(dicionario2) # adicionar as chaves novas e atualiza as que já existem
print(dicionario1)
print(dicionario2)

dicionarioA = {"a" : 1 , "b" : 2 , "c" : 3}
dicionarioB = {"c" : 4 , "d" : 5}
# O operado | so existe apartir da versão 3.9 do python
juntar = dicionarioA | dicionarioB
print(juntar)
print(dicionarioA)
print(dicionarioB)