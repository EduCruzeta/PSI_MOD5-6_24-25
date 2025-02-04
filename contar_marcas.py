"""Calcular quantos carros de cada marca existem num array guardando num dicionario a marca e o nº de carros
Ex: :{"bmw" : 2,
    "tesla" : 2,
    "peugeot" : 1,
    ...}"""

import numpy as np

carros = np.array(["bmw","tesla","peugeot","ford","tesla","mercedes","bmw","volvo"])

marcas = {}

# ciclo para precorrer o array das marcas
for carro in carros:
    # verificar se a marca já existe no dicionario
    if carro in marcas:
        marcas[carro] = marcas[carro] + 1
    else:
        marcas[carro] = 1

print(marcas)

#--------------------------------------------------------------#

carros = np.array(["bmw","tesla","peugeot","ford","tesla","mercedes","bmw","volvo"])

marcas = {}

# ciclo para precorrer o array das marcas
for carro in carros:
    marcas[carro] = marcas.get(carro,0) + 1

print(marcas)