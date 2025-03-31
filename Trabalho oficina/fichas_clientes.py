"""
Módulo responsável pela gestão das fichas dos clientes
"""
import utils, os

# dados de exemplo para as listas dos clientes
clientes = [
{"propriatario":"joão alves","veiculos":[{"matricula":"AA-12-BB","modelo":"Toyota Corolla","estado": "Pronto","pecas":""},{"matricula":"AA-67-hj","modelo":"Toyota prius","estado": "em espera","pecas":""}]},
{"propriatario":"ana silva","veiculos":[{"matricula":"BB-12-CB","modelo":"honda civic","estado": "Em espera","pecas":""}]},
{"propriatario":"joão","veiculos":[{"matricula":"IA-82-HB","modelo":"jaguar","estado": "Em espera","pecas":""}]}]

# lista dos campos privados
lista_campos_privados = ["estado","pecas"]


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
    # pedir se deseja criar uma ficha ou inserir um novo carro
    op = utils.Menu(["Adicionar nova ficha","Adicionar mais 1 carro","Voltar"],"Escolha: ")
    if op == 3:
        return
    if op == 2:
        # pesquisar a ficha
        ficha = PesquisarFicha()
        op = utils.ler_string(1,"deseja inserir um novo veiculo a sua ficha? s/n")
        if op in "nN":
            return
        matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
        if "-" not in matricula:
            print("Matricula invalida!")
            return
        modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

        novo = {"matricula": matricula, "modelo": modelo,"estado": "Em espera","pecas":""}

        ficha["veiculos"].append(novo)
        return
    # introduzir o nome do propriatario
    propriatario = utils.ler_string(3,"Introduza o nome do propriatário do veículo: ")

    # introduzir a matricula do carro
    matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
    if "-" not in matricula:
        print("Matricula invalida!")
        return

    # introduzir a marca do carro ou modelo
    modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

    # criar o novo dicionario
    novo = {"propriatario":propriatario,"veiculos":[{"carro":1,"matricula": matricula, "modelo": modelo,"estado": "Em espera","pecas":""}]}
    
    # colocar o novo dicionario na lista dos carros
    clientes.append(novo)
    print(f"Ficha cliente registrada com sucesso.")

def Editar():
    """Função responsável por editar a ficha do cliente"""
    # Pesquisar a ficha a editar
    ficha_editar = PesquisarFicha() 
    # verificar se encontrou algum
    if ficha_editar == None:
        print("Ficha não encontrado.")
        return
    # escolher o campo a editar
    op = utils.Menu(["Editar propriatário","Editar carro","Voltar"],"Escolha")
    if op == 1:
        ficha_editar["propriatario"] = utils.ler_string(3,"Introduza o novo nome do propriatario: ")
        print("Edição concluída com sucesso.")
        return
    if op == 2:
        # verificar se tem mais que 1 carro
        if len(ficha_editar["veiculos"]) >= 2:
            # escolher qual dos carros quer editar
            carroeditar = PesquisarCarro(ficha_editar)
        else:
            carroeditar = ficha_editar["veiculos"][0]

        lista_campos = list(carroeditar.keys())
        # remover os campos privados
        for c in lista_campos_privados:
            lista_campos.remove(c)
        op = utils.Menu(lista_campos,"Qual o campo a editar? ")
        campo = lista_campos[op-1]
        # mostrar o valor atual do campo a editar
        print(f"O campo {campo} tem o seguinte valor {carroeditar[campo]}")
        novo_valor = utils.ler_string(3,"Novo valor: ")
        # guardar o novo valor
        ficha_editar[campo] = novo_valor
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
    # confirmar se é a ficha que deseja apagar
    print(f"propriatário:{ficha_apagar["propriatario"]}")
    op = input("Deseja apagar esta ficha (s/n)?: ")
    if op in "sS":
        # verificar se tem algum carro em manutenção
        carros = ficha_apagar["veiculos"] 
        for carro in carros:
            if carro["estado"] == "Em manutenção":
                print("A ficha do cliente não pode ser removida o cliente tem veículos em manutenção.")
        clientes.remove(ficha_apagar)
    print(f"Ficha removida com sucesso. Tem {len(clientes)} ficha/s de carro disponiveis.")

def Listar():
    """Função responsável por listar a ficha dos clientes registrados"""
    print("-"*20)
    print("Lista de Clientes")
    print("-"*20)
    for ficha in clientes:
        for carro in ficha["veiculos"]:
            print(f"Propriatário:{ficha["propriatario"]} | Modelo:{carro["modelo"]} |  Matricula:{carro["matricula"]}")
            print("-"*40)

def PesquisarFicha():
    """Devolver a ficha do cliente que corresponde ao nome"""
    # pedir o nome do propriatario a pesquisar
    pesquisa = utils.ler_string(2,"Introduza o nome do propriatario a pesquisar: ")
    # percorrer a lista das fichas ate encontrar o cliente
    for ficha in clientes:
        if pesquisa.lower() in ficha["propriatario"].lower():
            op = utils.ler_string(1,f"A ficha é do propriatário/a {ficha["propriatario"]} com o carro {ficha["veiculos"][0]["modelo"]}? s/n: ")
            if op in "sS":
                return ficha
                
def PesquisarCarro(ficha):
    """Devolver o carro que o utilizador deseja"""
    # percorrer a lista das fichas ate encontrar o cliente
    for carro in ficha["veiculos"]:
        op = utils.ler_string(1,f"Deseja editar o {carro["modelo"]} s/n? :")
        if op in "sS":
            return carro
