"""
Módulo de gestão dos livros
"""
import utils

# lista dos livros
livros = []

# Menu Livros
def MenuLivros():
    """Submenu para gerir os livros"""
    op = 0
    while op != 6:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu Livros")
        if op == 6:
            break

# Adicionar Livro

# Editar Livro

# Apagar Livro

# Listar Livros

# Pesquisar Livros