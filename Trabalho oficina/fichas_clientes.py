"""
Módulo responsável pela gestão das fichas dos clientes
"""
import utils, os, oficina, pickle

# dados de exemplo para as listas dos clientes
clientes = []

# set de todas as matriculas para evitar repetidas
todas_matriculas = ["AA-MM-hh","BB-12-CB","IA-82-HB","AA-67-hj"]

# lista dos campos privados
lista_campos_privados = ["pecas","nif"]

def MenuClientes():
    """Submenu para gerir as fichas dos clientes"""
    os.system("cls")
    op = 0
    while op != 5:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Voltar"],"Menu ficha clientes")
        if op == 5:
            GuardarDados()
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Editar()
        if op == 4:
            Apagar()

def Adicionar():
    """Função responsável por adicionar a ficha do cliente"""
    # perguntar se deseja criar uma ficha ou inserir um novo carro
    op = utils.Menu(["Adicionar nova ficha","Adicionar mais 1 carro","Voltar"],"Escolha: ")
    if op == 3:
        return
    if op == 2:
        # pesquisar a ficha
        ficha = PesquisarFicha()

        # verificar se a ficha existe
        if ficha == None:
            print("Não tem ficha registrada crie uma ficha primeiro.")
            return
        
        # perguntar se quer inserir um carro novo
        op = utils.ler_string(1,"deseja inserir um novo carro a sua ficha? s/n")
        if op in "nN":
            return
        
        # pedir a matricula do carro
        matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
        if "-" not in matricula:
            print("Matricula invalida!")
            return
    
        # verificar se a matricula ja existe
        for matricula_verificar in todas_matriculas:
            if matricula == matricula_verificar:
                print("Essa matricula já existe.")
                return

        # adiconar a matricula a lista de matriculas
        todas_matriculas.append(matricula)

        modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

        novo = {"matricula": matricula, "modelo": modelo, "pecas":"","nif":ficha["nif"]}

        # adicionar o novo carro a lista dos carros da ficha do cliente
        ficha["veiculos"].append(novo)
        return
    
    # introduzir o nome do proprietario
    numeros ="0123456789"
    proprietario = utils.ler_string(3,"Introduza o nome do proprietário do veículo: ")
    for numero in numeros:
        if numero in proprietario:
            print("Nome invalido! O nome não pode conter números.")
            return

    # pedir o nif do proprietario
    nif = utils.ler_numero_inteiro("Introduza o nif: ")

    # pedir a matricula do carro
    matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
    if "-" not in matricula:
        print("Matricula invalida!")
        return
    
    # verificar se a matricula ja existe
    for matricula_verificar in todas_matriculas:
        if matricula == matricula_verificar:
            print("Essa matricula já existe.")
            return
        
    # adiconar a matricula a lista de matriculas
    todas_matriculas.append(matricula)

    # introduzir a marca do carro ou modelo
    modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

    # criar o novo dicionario
    # retirei o campo estado do carro TODO
    novo = {"proprietario":proprietario,"nif":nif,"veiculos":[{"matricula": matricula, "modelo": modelo,"pecas":"","nif":nif}]}
    
    # colocar o novo dicionario na lista dos carros
    clientes.append(novo)
    print(f"Ficha cliente registrada com sucesso.")

def Editar():
    """Função responsável por editar a ficha do cliente"""
    # Pesquisar a ficha a editar
    ficha_editar = PesquisarFicha() 

    # verificar se encontrou algum
    if ficha_editar == None:
        print("Ficha não encontrada.")
        return
    
    # escolher o campo a editar
    op = utils.Menu(["Editar proprietário","Editar carro","Voltar"],"Escolha")
    if op == 3:
        return
    if op == 1:
        # editar o nome do proprietário
        ficha_editar["proprietario"] = utils.ler_string(3,"Introduza o novo nome do proprietario: ")
        print("Edição concluída com sucesso.")
        return
    if op == 2:
        # verificar se tem mais que 1 carro
        if len(ficha_editar["veiculos"]) >= 2:
            # escolher qual dos carros quer editar
            carroeditar = PesquisarCarro(ficha_editar)
            if carroeditar == None:
                print("Carro não encontrado")
        else:
            carroeditar = ficha_editar["veiculos"][0]

        # passar as chaves do dicionario para a lista 
        lista_campos = list(carroeditar.keys())

        # remover os campos privados
        for c in lista_campos_privados:
            lista_campos.remove(c)

        op = utils.Menu(lista_campos,"Qual o campo a editar? ")
        campo = lista_campos[op-1]

        # mostrar o valor atual do campo a editar
        print(f"O campo {campo} tem o seguinte valor {carroeditar[campo]}")
        novo_valor = utils.ler_string(3,"Novo valor: ")
        if campo == "matricula":
            if "-" not in novo_valor:
                print("Matricula invalida!")
                return
            
        # guardar o novo valor
        carroeditar[campo] = novo_valor
        print("Edição concluída com sucesso.")

def Apagar():
    """Função responsável por apagar a ficha do cliente"""
    # verificar se a lista das fichas está vazia
    if len(clientes) == 0:
        print("Não tem mais fichas de clientes para remover. ")
        return

    # pesquisar a ficha do cliente a apagar
    ficha_apagar = PesquisarFicha()

    # verificar se encontrou a ficha
    if ficha_apagar == None:
        print("Nenhuma ficha encontrada.")
        return

    # verificar se tem mais que um carro
    if len(ficha_apagar["veiculos"]) >= 2:
        # pedir se deseja apagar uma ficha ou apagar um carro
        print("Tem mais de 1 carro deseja: ")
        op = utils.Menu(["Apagar carro","Apagar ficha","Voltar"],"Escolha:")
        if op == 3:
            return
        if op == 1:
            # encontrar qual dos carros deseja apagar
            carroapagar = PesquisarCarro(ficha_apagar)
            # verificar se o carro está em manutenção
            for carro_manutencao in oficina.manutencoes:
                if carroapagar["matricula"] in carro_manutencao["matricula"]:
                    print("O carro está em manutenção não pode ser apagado.")
                    return
            # verificar se realmente quer apagar aquele carro
            op = utils.ler_string(1,f"Deseja apagar o carro: modelo:{carroapagar["modelo"]} | matricula: {carroapagar["matricula"]} s/n:")
            if op in "sS":
                ficha_apagar["veiculos"].remove(carroapagar)
                print("Carro excluido com sucesso.")
                return

    # confirmar se é a ficha que deseja apagar
    print(f"proprietário:{ficha_apagar["proprietario"]}")
    op = input("Deseja apagar esta ficha (s/n)?: ")
    if op in "sS":
        # verificar se tem algum carro em manutenção
        carro = ficha_apagar["veiculos"][0]
        for carro_manutencao in oficina.manutencoes:
            if carro["matricula"] in carro_manutencao["matricula"]:
                print("A ficha do cliente não pode ser removida o cliente tem o carro em manutenção.")
                return
        clientes.remove(ficha_apagar)
        print(f"Ficha removida com sucesso. Tem {len(clientes)} ficha/s de carro disponiveis.")
    else:
        return

def Listar():
    """Função responsável por listar a ficha dos clientes registrados"""
    print("-"*20)
    print("Lista de Clientes")
    print("-"*20)
    for ficha in clientes:
        for carro in ficha["veiculos"]:
            print(f"proprietário:{ficha["proprietario"]} | Modelo:{carro["modelo"]} |  Matricula:{carro["matricula"]}")
            print("-"*40)

def PesquisarFicha():
    """Devolver a ficha do cliente que corresponde ao nome"""
    # pedir o nome do proprietario a pesquisar
    pesquisa = utils.ler_string(2,"Introduza o nome do proprietario a pesquisar: ")

    # percorrer a lista das fichas ate encontrar o cliente
    for ficha in clientes:
        if pesquisa.lower() in ficha["proprietario"].lower():
            op = utils.ler_string(1,f"A ficha é do proprietário/a {ficha["proprietario"]} com o carro {ficha["veiculos"][0]["modelo"]}? s/n: ")
            if op in "sS":
                return ficha
                
def PesquisarCarro(ficha):
    """Devolver o carro que o utilizador deseja"""
    # percorrer a lista das fichas ate encontrar o cliente
    for carro in ficha["veiculos"]:
        op = utils.ler_string(1,f"Qual carro deseja - {carro["modelo"]} s/n? :")
        if op in "sS":
            return carro
        
def GuardarDados():
    global clientes
    global todas_matriculas
    # primeiro guardar os dados dos carros

    lista_carros = []
    # criar uma lista sem referencias para dicionarios de outras listas
    for ficha in clientes:
        for carro in ficha["veiculos"]:
            #substituir a referencia para a lista de leitores por o id e dos livros
            novo = {"modelo":carro["modelo"],
                    "matricula":carro["matricula"],
                    "pecas":carro["pecas"],
                    "nif":carro["nif"]}
            lista_carros.append(novo)

    with open("Carros.dat","wb") as ficheiro:
        pickle.dump(lista_carros,ficheiro)

    lista_proprietario = []
    # criar uma lista sem referencias para dicionarios de outras listas
    for ficha in clientes:
        #substituir a referencia para a lista de leitores por o id e dos livros
        novo = {"proprietario":ficha["proprietario"],
                "nif":ficha["nif"]}
        lista_proprietario.append(novo)
        print(ficha)

    with open("Proprietarios.dat","wb") as ficheiro:
        pickle.dump(lista_proprietario,ficheiro)

    # guardar a lista de matriculas já registradas
    lista_matriculas = []

    for matricula in todas_matriculas:
        lista_matriculas.append(matricula)

    with open("matriculas.dat","wb") as ficheiro:
        pickle.dump(lista_matriculas,ficheiro)

def LerDados():
    global clientes
    global todas_matriculas

    lista_carros = []
    lista_proprietarios = []

    if os.path.exists("Carros.dat") == False:
        return
    
    with open("Carros.dat","rb") as ficheiro:
        lista_carros = pickle.load(ficheiro)

    with open("Proprietarios.dat","rb") as ficheiro:
        lista_proprietarios = pickle.load(ficheiro)

    with open("matriculas.dat","rb") as ficheiro_matriculas:
        todas_matriculas = pickle.load(ficheiro_matriculas)
    
    # criar a lista dos clientes novamente

    for proprietario in lista_proprietarios:
        lista_carros_proprietario = []
        for carro in lista_carros:
            if carro["nif"] == proprietario["nif"]:
                lista_carros_proprietario.append(carro)
                novo = {"proprietario":proprietario["proprietario"],"nif":proprietario["nif"],"veiculos":lista_carros_proprietario}
                clientes.append(novo)