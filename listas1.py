"""
Listas-Estrutura de dados dinâmica (nº de elementos pode aumentar e diminuir), não homogenea 
(pode ter elementos com diferentes tipo de dados, incluindo, mutáveis - listas, dicionarios, arrays, etc)
"""
# defenir uma lista
minha_lista = [] # lista vazia
minha_lista2 = [1,2,3,"quatro"]
minha_lista3 = list({1,2,3})
lista_de_cinco = list(range(5))
print(minha_lista,minha_lista2,minha_lista3,lista_de_cinco)
# listas são referencias


x = 10
y = x # criar uma variavel nova e copia o valor dessa variavel
x = 11
print(x,y)


lista_x = [1,2,3]
lista_y = lista_x # as duas variaveis "apontam" para o mesmo conjunto de dados
lista_x[1] = 10
print(lista_x,lista_y)
# para criar uma cópia da lista
lista_z = lista_x[:]  # cria uma lista nova e copia todos os valores
lista_x[1] = 5
print(lista_x,lista_z)


# lista de valores da lista
print(lista_z[0]) # mostrar o primeiro elemento da lista
lista_k=[1,2,[10,20]] # lista com uma lista incorporada
# mostrar o primeiro valor da lista incorporada
print(lista_k[2][0])

# dicionario incorporado
notas = [{"joaquim":10},{"maria":15},{"antónio":12}]
# Mostrar a nota do antónio
print(notas[2]["antónio"])