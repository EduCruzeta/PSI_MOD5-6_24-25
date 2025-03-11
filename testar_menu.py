"""Programa para testar a função Menu
1.Adicionar
2.Remover
3.Listar
4.Terminar
"""
import utils

while True:
    op = utils.Menu(("Adicionar","Remover","Listar","Terminar"))
    if op == 4:
        break
    if op == 1:
        print("Adicionar")
    if op == 2:
        print("Remover")
    if op == 3:
        print("Listar")