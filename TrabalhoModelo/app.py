"""
Trabalho Modelo - Módulo 6
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão dos livros (CRUD)
    - Gestão dos leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (empréstimos em atraso, top livros, top mês, top leitores, ...)
"""
import utils,livros

# Deve estar true quando em testes e False quando em produção
DEBUG = True


def MenuPrincipal():
    if DEBUG:
        livros.Configurar()
    op = 0
    while op != 5:
        op = utils.Menu(["Livros","Leitores","Empréstimos/Devoluções","Estatísticas","Sair"],"Menu Principal")
        if op == 5:                 
            break
        if op == 1:
            print("#-------------------------#")
            livros.MenuLivros()


if __name__=="__main__":
    MenuPrincipal()