"""
Módulo de gestão dos livros
"""
import utils

# lista dos livros
livros = []

# lista de livros de exemplo

exemplo_livros = [
    {"id":1,"titulo": "livro 1","autor": "a","assunto" : "assunto 1","editora" : "a","ano" : 2000,"estado": "disponivel","leitor": None,"nr_emprestimos" : 0},
    {"id":2,"titulo": "livro 2","autor": "b","assunto" : "assunto 2","editora" : "b","ano" : 2020,"estado": "disponivel","leitor": None,"nr_emprestimos" : 0},
    {"id":3,"titulo": "livro 3","autor": "c","assunto" : "assunto 3","editora" : "c","ano" : 1990,"estado": "disponivel","leitor": None,"nr_emprestimos" : 0}
]

def Configurar():
    """Insere dados de exemplo"""
    livros.extend(exemplo_livros)

# Menu Livros
def MenuLivros():
    """Submenu para gerir os livros"""
    op = 0
    while op != 6:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu Livros")
        print("#-------------------------#")
        if op == 6:
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Listar(livros)
        if op == 3:
            pass
        if op == 4:
            pass
        if op == 5:
            pass

# Adicionar Livro
def Adicionar():
    print("#### Adicionar livro novo ###")
    # Título
    titulo = utils.ler_string(3,"Introduza o título: ")
    # Autor
    autor = utils.ler_string(3,"Introduza o autor: ")
    # Assunto
    assunto = utils.ler_string(3,"Introduza o assunto: ")
    # Editora
    editora = utils.ler_string(3,"Introduza a editora: ")
    # Ano edição
    ano = utils.ler_numero_inteiro_limites(1500,2030,"Introduza o ano de edição: ")
    # id
    id = 1
    if len(livros)>0:
        id = livros[len(livros)-1]["id"]+1 # Codigo vai gerar o id apartir do id do ultimo livro
    novo = {
        "id":id,
        "titulo": titulo,
        "autor": autor,
        "assunto" : assunto,
        "editora" : editora,
        "ano" : ano,
        "estado": "disponivel",
        "leitor": None,
        "nr_emprestimos" : 0

    }
    livros.append(novo)
    print(f"Livro registrado com sucesso. Tem {len(livros)} livros")

# Editar Livro

# Apagar Livro

# Listar Livros
def Listar(lista_a_listar):
    """Função para listar todos os livros"""
    print("#"*40)
    print("Lista de livros")
    print("#"*40)
    for livro in lista_a_listar:
        print(f"Id:{livro["id"]} Nome:{livro["titulo"]} Assunto:{livro["assunto"]} Estado:{livro["estado"]}")
        print("-"*80)

# Pesquisar Livros
def Pesquisar():
    """Devolver a lista dos livros que correspondem a um critério"""
    # Deixar o utilizador escolher o campo de pesquisa
    op = utils.Menu(["Autor","Título"],"Escolha o campo de pesquisa:")
    # Criar uma lista para os resultados
    l_resultados = []
    if op == 1:
        campo = "autor"
    else:
        campo = "titulo"
    pesquisa = utils.ler_string(3,f"{campo} a pesquisar: ")
    # Adicionar à lista os livros que correspondem ao resultado da pesquisa
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            l_resultados.append(livro)
    Listar(l_resultados)