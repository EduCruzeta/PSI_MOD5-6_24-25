"""
Módulo responsável por gerir as peças adicionar novas peças editar ou remover vai ter sistema de stock com ficheiro de texto
"""
import utils , os
lista_pecas = []
NOME_FICHEIRO = "Peças.txt"

def MenuPecas():
    """Submenu para gerir as peças"""
    os.system("cls")
    op = 0
    while op != 6:
        op = utils.Menu(["Adicionar","Editar","Listar","Listar com pesquisada","Remover","Voltar"],"Menu Peças")
        if op == 6:
            Guardar()
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Editar()
        if op == 3:
            Listar()
        if op == 4:
            ListarPesquisa()
        if op == 5:
            Remover()

def Adicionar():
    """Função para adicionar peças novas a oficina"""
    peca = input("Insira a nova peça: ")
    preco = utils.ler_numero_decimal_limites(0,9999999,"Insira o preço da peça: ")
    stock = utils.ler_numero_inteiro_limites(0,10000,"Insira a quantidade de stock disponivel: ")

    novo = {"peça" : peca,"preço" : preco, "stock" : stock}

    lista_pecas.append(novo)
    Guardar()

def Editar():
    """Função para editar alguma peça ou o seu preço"""
    peca_editar = PesquisarPeca()

    # verificar se encontrou algum
    if peca_editar == None:
        print("Peça não encontrada.")
        return
        
    # escolher o campo a editar
    op = utils.Menu(["Editar nome da peça","Editar preço","Editar stock","Voltar"],"Escolha")
    if op == 4:
        return
    if op == 1:
        # editar o nome da peça
        peca_editar["peça"] = utils.ler_string(3,"Introduza o novo nome da peça: ")
        print("Edição concluída com sucesso.")
        Guardar()
        return
        
    if op == 2:
        # editar o preço da peça
        peca_editar["preço"] = utils.ler_numero_decimal(f"Introduza o novo valor da peça {peca_editar["peça"]}: ")
        print("Edição concluída com sucesso.")
        Guardar()
        return
        
    if op == 3:
        # editar o stock da peça
        peca_editar["stock"] = utils.ler_numero_inteiro(f"Introduza o stock da peça {peca_editar["peça"]}: ")
        print("Edição concluída com sucesso.")
        Guardar()
        return

def Listar():
    """Função para listar as peças e ver o stock"""

    if not lista_pecas:
        print("Ainda não tem peças")
        return
    
    print("-"*20)
    print("Lista de Peças")
    print("-"*20)
    for peca in lista_pecas:
        print(f"Peça - {peca["peça"]} | Preço - {peca["preço"]}€ | Stock - {peca["stock"]}")
        print("-"*40)

def Remover():
    """função para remover peças do stock"""
    global lista_pecas

    peca_remover = PesquisarPeca()

    # verificar se encontrou algum
    if peca_remover == None:
        print("Peça não encontrada.")
        return
    
    op = input(f"Deseja remover {peca_remover["peça"]} da lista? s/n ")
    
    if op in "sS":
        lista_pecas.remove(peca_remover)
        Guardar()
    else:
        return
    
def ListarPesquisa():
    """Função responsavel por listar a peça pesquisada apenas"""
    
    peca_pesquisar = PesquisarPeca()

    # verificar se encontrou algum
    if peca_pesquisar == None:
        print("Peça não encontrada.")
        return
    
    print(f"Peça-{peca_pesquisar["peça"]} | Preço-{peca_pesquisar["preço"]}€ | Stock-{peca_pesquisar["stock"]}")

def PesquisarPeca():
    """função responsavel por pesquisar a peça"""
    if not lista_pecas:
        print("Ainda não tem peças")
        return
    
    # pedir o nome da peça a pesquisar
    pesquisa = utils.ler_string(0,"Introduza o nome da peça a pesquisar (Enter para voltar): ")

    if pesquisa == "":
        return

    # percorrer a lista das fichas ate encontrar o cliente
    for peca in lista_pecas:
        if pesquisa.lower() in peca["peça"].lower():
            op = utils.ler_string(1,f"A peça é {peca["peça"]}? s/n: ")
            if op in "sS":
                return peca
            
def Ler():
    """Função responsavel por ler as peças assim que o programa abrir"""
    global lista_pecas

    if os.path.exists(NOME_FICHEIRO) == False:
        return
    
    #tamanho = os.path.getsize(NOME_FICHEIRO)

    #if tamanho >= 0:
        return
    
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            linha = linha.replace("\n","")
            partes = linha.split("|")

            nome = partes[0][7::].strip()
            preco = partes[1][8::].strip()
            stock = partes[2][8::].strip()

            novo = {"peça":nome,"preço":preco,"stock":stock}
            lista_pecas.append(novo)
    
def Guardar():
    """Função responsável por guardar a lista atual da peças em ficheiro de texto"""
    global lista_pecas

    with open(NOME_FICHEIRO,"w",encoding="utf-8") as ficheiro:
        for peca in lista_pecas:
            if int(peca["stock"]) == 0:
                linha = (f"Peça - {peca["peça"]} | Preço - {peca["preço"]} | [Sem Stock] - {peca["stock"]}\n")
                ficheiro.write(linha)
            else:
                linha = (f"Peça - {peca["peça"]} | Preço - {peca["preço"]} | Stock - {peca["stock"]}\n")
                ficheiro.write(linha)

def Retirarstock(nome,quantidade):
    global lista_pecas

    for peca in lista_pecas:
        if peca["peça"] == nome:
            stock = peca["stock"] 
            if int(stock) == 0:
                print("Não tem mais stock desta peça.")
                return
            stock = int(stock) - quantidade
            peca["stock"] = str(stock)
            Guardar()

