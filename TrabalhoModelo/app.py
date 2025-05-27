"""
Trabalho Modelo - Módulo 7
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão dos livros (CRUD)
    - Gestão dos leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (empréstimos em atraso, top livros, top mês, top leitores, ...)

Para o módulo 7 foi adicionado a materialização dos dados
"""
import utils,livros,leitores, emprestimos, os , estatísticas

# Deve estar true quando em testes e False quando em produção
DEBUG = False

def MenuPrincipal():
    if DEBUG:
        livros.Configurar()
        leitores.Configurar()
    op = 0
    # ler dados dos ficheiros
    livros.LerDados()
    leitores.LerDados()
    emprestimos.LerDados()
    while op != 5:
        os.system("cls")
        op = utils.Menu(["Livros","Leitores","Empréstimos/Devoluções","Estatísticas","Sair"],"Menu Principal")
        if op == 5:                 
            break
        if op == 1:
            livros.MenuLivros()
        if op == 2:
            leitores.MenuLeitores()
        if op == 3:
            emprestimos.MenuEmprestimos()
        if op == 4:
            estatísticas.MenuEstatisticas()

    # guardar os dados
    livros.GuardarDados()
    leitores.GuardarDados()
    emprestimos.GuardarDados()
    
if __name__=="__main__":
    MenuPrincipal()