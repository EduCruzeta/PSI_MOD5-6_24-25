"""
Módulo de gestão dos livros
"""
import utils

# lista dos livros
livros = []

# lista de livros de exemplo

exemplo_livros = [
    {"id":1,"titulo": "livro 1","autor": "autor 1","assunto" : "assunto 1","editora" : "a","ano" : "2000","estado": "disponivel","leitor": None,"nr_emprestimos" : 0},
    {"id":2,"titulo": "livro 2","autor": "autor 2","assunto" : "assunto 2","editora" : "b","ano" : "2020","estado": "disponivel","leitor": None,"nr_emprestimos" : 0},
    {"id":3,"titulo": "livro 3","autor": "autor 3","assunto" : "assunto 3","editora" : "c","ano" : "1990","estado": "disponivel","leitor": None,"nr_emprestimos" : 0}
]

# Campos que nao podem ser editados pelo utilizador
lista_campos_privados = ["id","estado","leitor","nr_emprestimos"]

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
            Editar()
        if op == 4:
            Apagar()
        if op == 5:
            Pesquisar_listar()

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
def Editar():
    # Pesquisar o livro a editar
    livros_editar = Pesquisar()
    # mostrar os dados de cada livro encontrado
    if len(livros_editar) == 0:
        print("Não foram encontrados livros.")
        return
    # mostrar os livros encontrados
    Listar(livros_editar)
    # permetir alterar os dados
    id = utils.ler_numero_inteiro("Introduza o id do livro para editar ou 0 (zero) para cancelar: ")
    if id == 0:
        return
    # livro com o id indicado
    livro = None
    for l in livros_editar:
        if l["id"] == id:
            livro = l
            break
    if livro == None:
        print("O id indicado não existe")
        return  
    # escolher o campo a editar
    lista_campos = list(livro.keys())
    # remover os campos privados
    for c in lista_campos_privados:
        lista_campos.remove(c)
    op = utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo = lista_campos[op-1]
    # mostrar o valor atual do campo a editar
    print(f"O campo {campo} tem o valor {livro[campo]}")
    novo_valor = utils.ler_string(3,"Novo valor: ")
    # guardar o novo valor
    livro[campo] = novo_valor
    print("Edição concluída com sucesso.")

# Apagar Livro
def Apagar():
    #verificar se a lista está vazia
    if len(livros) == 0:
        print("Não tem mais livros para remover. ")
        return
    # pesquisar os livros com titulo semelhante
    l_livros = Pesquisar()
    # verificar se nao encontrou nenhum
    if len(l_livros) == 0:
        print("Não foi encontrado nenhum livro com esse nome.")
        return
    # confirmar para cada um dos livros se deseja apagar
    for livro in l_livros:
        print(f"Id:{livro["id"]} titulo:{livro["titulo"]}")
        op = input("Deseja apagar este livro (s/n)?: ")
        if op in "sS":
            #TODO confirmar se o livro não está emprestado
            livros.remove(livro)
            break
    print(f"Livro removido com sucesso. Tem {len(livros)} livros.")
        
# Listar Livros
def Listar(lista_a_listar):
    """Função para listar todos os livros"""
    print("#"*40)
    print("Lista de livros")
    print("#"*40)
    for livro in lista_a_listar:
        print(f"Id:{livro["id"]} Nome:{livro["titulo"]} Assunto:{livro["assunto"]} Estado:{livro["estado"]}")
        print("-"*80)

# pesquisar e listar
def Pesquisar_listar():
    resultado = Pesquisar()
    Listar(resultado)

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
    return l_resultados