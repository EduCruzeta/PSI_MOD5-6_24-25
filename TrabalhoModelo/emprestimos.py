"""
Módulo Empréstimos e devoluções
"""

import utils, livros, leitores
from datetime import datetime,timedelta
import os

# livro ({}), leitor({}), data_emprestimo, data_devolução, estado
emprestimos = []

def MenuEmprestimos():
    os.system("clear")
    op = 0
    while op != 4:
        op = utils.Menu(["Empréstimos","Devoluções","Listar","Voltar"],"Menu de empréstimos/devoluções")
        if op == 4:
            break
        if op == 1:
            Emprestimos()
        if op == 2:
            Devolucao()
        if op == 3:
            Listar()

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
            return
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
    novo["estado"] = True # Emprestimo está a decorrer
    emprestimos.append(novo)
    # atualizar o estado do livro
    novo["livro"]["estado"] = "emprestado"
    novo["livro"]["leitor"] = novo["leitor"]
    print("Empréstimo registado com sucesso.")
    print(f"Livro emprestado: {novo["livro"]}")
    print(f"Leitor: {novo["leitor"]}")

def Devolucao():
    pass
    # ler o id do livro a devolver
    id_livro = utils.ler_numero_inteiro("Indique o id do livro a devolver: ")
    # verificar se o livro esta emprestado
    livro = livros.Get_livro(id_livro)
    if livro == None:
        print("Não existe nenhum livro com o id indicado.")
    if livro["estado"] != "emprestado":
        print("Esse livro não está emprestado")
    # verificar se a devolcao esta dentro do prazo
    emprestimo_devolver = None
    for emprestimo in emprestimos:
        if emprestimo["livro"] == livro and emprestimo["estado"] == True:
            emprestimo_devolver = emprestimo
    if emprestimo == None:
        print("Empréstimo não encontrado.")
        return
    data_devolucao = emprestimo_devolver["data_devolucao"]
    data_atual = datetime.now()
    # sugestão do afonso
    idata_atual = int(data_atual.strftime("%Y%m%d"))
    idata_devolucao = int(datetime.strptime(data_devolucao,"%Y-%m-%d").strftime("%Y%m%d"))
    if idata_atual > idata_devolucao:
        print("Devolução fora do prazo")
        # registar se houve infração do leitor
        emprestimo_devolver["leitor"]["infracoes"] += "Entrega fora de prazo"
    # atualizar se o nr de emprestimos do livro
    livro["nr_emprestimos"] += 1
    # mudar o estado do livro
    livro["estado"] = "disponivel"
    livro["leitor"] = None
    # mudar o estado de emprestimo
    emprestimo_devolver["estado"] = False
    print("Devolução concluída com sucesso.")
    
def Listar():
    # perguntar se pretende ver todos os empréstimos ou só os emprestimos por concluír
    op = utils.ler_string(1,"Listar [T]odos ou só por [C]oncluír: ")
    for emp in emprestimos:
        if op in "tT" or (op in "cC" and emp["estado"] == True):
            print(f"{emp["livro"]["titulo"]} {emp["leitor"]["nome"]} {emp["estado"]}")