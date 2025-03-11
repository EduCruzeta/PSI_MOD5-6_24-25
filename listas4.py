""" Listas por compreensão - criar uma lista com base num codigo 
que gera a lista a partir de outra lista ou uma função geradora"""
import random
lista_carros = ["ford","bmw","mercedes","renault","ferrari"]

# criar uma lista dos carros cuja marca começa por f
lista_marcas_f = []
for marca in lista_carros:
    if marca[0] == "f":
        lista_marcas_f.append(marca)

#lista aplicando um filtro à lista das marcas
lista_marcas_f_v2 = [marca for marca in lista_carros if marca[0] == "f"]

print(lista_marcas_f)
print(lista_marcas_f_v2)

# lista de nº sorteados

lista_numeros = [ random.randint(1,100) for i in range(10) ]
print(lista_numeros)