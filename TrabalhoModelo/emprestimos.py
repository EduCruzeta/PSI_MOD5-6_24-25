"""
Módulo Empréstimos e devoluções
"""

import utils

def MenuEmprestimos():
    op = 0
    while op != 3:
        op = utils.Menu(["Empréstimos","Devoluções","Voltar"],"Menu de empréstimos/devoluções")
        if op == 3:
            break
        if op == 1:
            Emprestimos()
        if op == 2:
            Devolucoes()

def Emprestimos():
    pass
# ler qual o livro a emprestar
# verificar se o livro pode ser emprestado
# ler qual o leitor que leva o livro
# verificar se o leitor pode levar o livro
# atualizar o estado do livro




def Devolucoes():
    pass
        
        