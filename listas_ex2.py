"""
Programa para gerir os livros de uma biblioteca e os seus empréstimos
"""
livros = ["livro 1","livro 2","livro 3","livro 4"]
emprestimos = []
livro = " "

# o programa deve terminar quando é inserido um titulo em branco ou quando não ha mais livros pra emprestar
while livro != "" :
    # avisar o utilizador quando o livro ja está emprestado ou nao existe
    if livro in livros:
        # remover da lista de livros para a lista de emprestimo
        livros.remove(livro)
        emprestimos.append(livro)
    elif livro in emprestimos:
        print(f"Livro está emprestado")
    else:
        print("Livro não existe")
    # mostrar os livros e os emprestimos
    print(livros,emprestimos)
    # verificar se ainda tem livros
    if len(livros) == 0:
        break
    # ler o título do livro a emprestar
    livro = input("Qual o livro a emprestar: ")
