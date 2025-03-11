"""
programar para sugerir uma aposta no euromilhões
deve sortear 5 nº entre 1 e 50 sem repetições
2 nº entre 1 e 12 tambem sme repetir
"""
import random


numeros_da_sorte = set()
estrelas = set()

while len(numeros_da_sorte) != 5:
    n = random.randint(1,50)
    numeros_da_sorte.add(n) 

while len(estrelas) != 2:
    n = random.randint(1,12)
    estrelas.add(n) 
    
print(estrelas)
print(numeros_da_sorte)

#--------------------------------------------------------#
numeros_lista = []
estrelas_listas = []

while len(numeros_lista) != 5:
    n = random.randint(1,50)
    if n in numeros_lista:
        continue
    numeros_lista.append(n) 

while len(estrelas_listas) != 2:
    n = random.randint(1,12)
    if n in estrelas_listas:
        continue
    estrelas_listas.append(n) 

print(numeros_lista)
print(estrelas_listas)


