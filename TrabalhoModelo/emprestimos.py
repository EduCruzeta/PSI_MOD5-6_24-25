"""
Módulo Empréstimos e devoluções
"""

import utils, livros, leitores
from datetime import datetime,timedelta

# livro ({}), leitor({}), data_emprestimo, data_devolução, estado
emprestimos = [""]

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
    # dados do emprestimo a adicionar a lista
    novo = {}
    # ler qual o livro a emprestar   
    print("Indique o livro a emprestar: ")
    livros_emprestar = livros.Pesquisar()
    if len(livros_emprestar) == 0:
        print("Nenhum livro encontrado. Tente novamente.")
        return
    elif len(livros_emprestar)>1:
        # mostrar os livros encontrados
        livros.Listar(livros_emprestar)
        # pedir o if do livro a emprestar
        id = utils.ler_numero_inteiro("Introduza o id do livro a emprestar: ")
        for livro in livros_emprestar:
            if livro["id"] == id:
                # verificar se o livro pode ser emprestados
                if livro["estado"] != "disponivel":
                    print("Esse livro está emprestado")
                    return
                novo["livro"] = livro
                break
        if "livro" not in novo:
            print("O Id indicado não existe")
            return
    else:
        # so encontrou 1 livro
        if livros_emprestar[0]["estado"] != "disponivel":
            print("Esse livro está emprestado")
            return
        novo["livro"] = livros_emprestar[0] 
    # ler qual o leitor que leva o livro
    print("Indique o Leitor: ")
    leitor_emprestimo = leitores.Pesquisar()
    if len(leitor_emprestimo) == 0:
        print("Leitor não encontrado")
        return
    elif len(leitor_emprestimo) > 1:
        print("Leitores encontrados: ")
        leitores.Listar(leitor_emprestimo)
        id = utils.ler_numero_inteiro("Indique o id do leitor: ")
        for leitor in leitor_emprestimo:
            if leitor["id"] == id:
                novo["leitor"] = leitor
                break
        if "leitor" not in novo:
            print("O id indicado não existe.")
    else:
        novo["leitor"] = leitor_emprestimo[0]
    # TODO verificar se o leitor pode levar o livro
    # registar o emprestimo com data de devolução
    data_atual = datetime.now()
    data_entrega = data_atual + timedelta(days=30)
    str_data_atual = data_atual.strftime("%Y-%m-%d")
    str_data_entrega = data_entrega.strftime("%Y-%m-%d")
    novo["data_emprestimo"] = str_data_atual
    novo["data_devolucao"] = str_data_entrega
    emprestimos.append(novo)
    # atualizar o estado do livro
    novo["livro"]["estado"] = "emprestado"
    novo["livro"]["leitor"] = novo["leitor"]
    print("Empréstimo registado com sucesso.")
    print(novo)

def Devolucao():
    pass
    # ler o id do livro a devolver
    # verificar se o livro esta emprestado
    # verificar se a devolcao esta dentro do prazo
    # registar se houve infração do leitor
    # atualizar se o nr de emprestimos do livro
    # mudar o estado do livro
    # mudar o estado de emprestimo

        
        