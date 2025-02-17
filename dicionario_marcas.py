"""
uma familia tem 3 pessoas. Pretende um programa que utiliza um dicionario 
para registar o nome de cada um e a marca do respetivo telemovel e computador.
O programa deve indicar qual a marca mais comum e se algum membro da familia tem somente uma marca.
"""
import numpy as np

marcas_todas = np.array(6)

marcas = {}

familia = {"p1":{"telemovel":"","computador":""},
           "p2":{"telemovel":"","computador":""},
           "p3":{"telemovel":"","computador":""}}

for i in familia:
    nome = input("insira o seu nome: ")
    telemovel = input(f"{nome} insira a marca do seu telemovel: ")
    computador = input(f"{nome} insira a marca do seu computador: ")
    familia[nome]= {"telemovel":telemovel}
    familia[nome]= {"computador":computador}


# ciclo para precorrer o array das marcas
for marca in marcas_todas:
    # verificar se a marca já existe no dicionario
    if marca in marcas_todas:
        marcas_todas[marca] = marcas[marca] + 1
    else:
        marcas[marca] = 1

print(marcas)







