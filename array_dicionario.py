import numpy as np
from datetime import datetime

"""
Programa para gerir os livros de uma biblioteca e os empréstimos
Menu: 1.Adicionar livro; 2.Listar todos; 3.Empréstimo; 4.Devolução; 5.Terminar
"""
MAX_LIVROS = 100

def ContagemLivros(livros):
    """Devolver o nº de posições preenchidas do array"""
    for p in range(MAX_LIVROS):
        if livros[p] == None:
            return p
    return MAX_LIVROS # array está cheio

def Livro():
    """Lê do utilizador os dados do livro novo e devolve um dicionario com esses dados"""
    nome = input("Introduza o nome do livro: ")
    tema = input("Introduza o tema do livro: ")
    leitor = None
    data_emp = None
    return {"nome":nome,"tema":tema,"leitor":leitor,"data_emp":data_emp}

def AdicionarLivro(livros):
    """Função para adicionar um livro novo ao array"""
    posicao = ContagemLivros(livros)
    # verificar se o array está cheio
    if posicao == MAX_LIVROS:
        print("Não pode inserir mais dados")
        return
    novo_livro = Livro()
    # adicionar o campo id
    novo_livro["id"] = posicao + 1
    # adiciona o novo livro na primeira posição livre do array
    livros[posicao] = novo_livro

def ListarLivros(livros):
    print(livros)

def Emprestimo(livros):
    id = int(input("Qual o id do livro a emprestar?: "))
    # validar o id
    if id < 1 or id > ContagemLivros(livros):
        print("O id introduzido não é valido")
        return
    # verificar se o livro ja está emprestado
    posicao = id - 1
    if livros[posicao]["leitor"] != None:
        print(f"Esse livro está emprestador ao leitor: {livros[posicao]["leitor"]}")
        return
    # ler o nome do leitor
    leitor = input("Qual o nome do leitor: ")
    data = datetime.now().strftime("%d-%m-%Y") # data como string em formato de dias portugues
    # registar o empréstimo
    livros[posicao]["leitor"] = leitor
    livros[posicao]["data_emp"] = data
    print("registrado com sucesso!")

def Devolucao(livros):
    id = int(input("Qual o id do livro a devolver?: "))
    # validar o id
    if id < 1 or id > ContagemLivros(livros):
        print("O id introduzido não é valido")
        return
    # verificar se o livro não está emprestado
    posicao = id - 1
    if livros[posicao]["leitor"] == None:
        print(f"Esse livro não está emprestado")
        return
    # registar o devolução
    livros[posicao]["leitor"] = None
    livros[posicao]["data_emp"] = None
    print("Livro devolvido com sucesso!")

def Menu():
    livros = np.empty(MAX_LIVROS,dtype=object)
    op = 0
    while op != 5:
        print("1.Adicionar livro\n2.Listar Todos\n3.Empréstimo\n4.Devolução\n5.Terminar")
        op = int(input("Opçãp: "))
        if op == 1:
            AdicionarLivro(livros)
        elif op == 2:
            ListarLivros(livros)
        elif op == 3:
            Emprestimo(livros)
        elif op == 4:
            Devolucao(livros)
        elif op == 5:
            break
        else:
            print("Opção inválida")

if __name__=="__main__":
    Menu()