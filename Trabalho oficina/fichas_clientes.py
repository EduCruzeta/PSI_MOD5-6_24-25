"""
Módulo responsável pela gestão das fichas dos clientes
"""
import utils, os, oficina

# dados de exemplo para as listas dos clientes
clientes = [
{"proprietario":"joão alves","veiculos":[{"matricula":"AA-MM-hh","modelo":"Toyota Corolla","pecas":""},{"matricula":"AA-67-hj","modelo":"Toyota prius","pecas":""}]},
{"proprietario":"ana silva","veiculos":[{"matricula":"BB-12-CB","modelo":"honda civic","pecas":""}]},
{"proprietario":"joão","veiculos":[{"matricula":"IA-82-HB","modelo":"jaguar","pecas":""}]}]

# lista dos campos privados
lista_campos_privados = ["pecas"]

def MenuClientes():
    """Submenu para gerir as fichas dos clientes"""
    os.system("cls")
    op = 0
    while op != 5:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Voltar"],"Menu ficha clientes")
        if op == 5:
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
        op = utils.ler_string(1,"deseja inserir um novo carro a sua ficha? s/n")
        if op in "nN":
            return
        matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
        if "-" not in matricula:
            print("Matricula invalida!")
            return
        modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

        novo = {"matricula": matricula, "modelo": modelo, "pecas":""}

        ficha["veiculos"].append(novo)
        return
    
    # introduzir o nome do proprietario
    proprietario = utils.ler_string(3,"Introduza o nome do proprietário do veículo: ")

    # introduzir a matricula do carro
    matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
    if "-" not in matricula:
        print("Matricula invalida!")
        return

    # introduzir a marca do carro ou modelo
    modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

    # criar o novo dicionario
    novo = {"proprietario":proprietario,"veiculos":[{"matricula": matricula, "modelo": modelo,"estado": "Em espera","pecas":""}]}
    
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
        print(ficha_editar)
        print("Edição concluída com sucesso.")

def Apagar():
    """Função responsável por apagar a ficha do cliente"""
    #verificar se a lista das fichas está vazia
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
