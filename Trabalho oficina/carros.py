"""
Módulo responsável pela gestão dos carros 
"""
import utils, os

# dados de exemplo para as listas
carros = [
{"matricula": "AA-12-BB", "modelo": "Toyota Corolla", "propriatario": "João Silva", "estado": "Em manutenção","pecas":"","cor":None},
{"matricula": "CC-45-DD", "modelo": "Honda Civic", "propriatario": "Maria Santos", "estado": "Em espera","pecas":"","cor":None}]

# lista dos carros


# lista dos campos privados
lista_campos_privados = ["cor","estado","pecas"]


def MenuCarros():
    """Submenu para gerir os carros"""
    os.system("cls")
    op = 0
    while op != 5:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Voltar"],"Menu Carros")
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
    """Função responsável por adicionar a ficha dos carros"""
    # introduzir o nome do propriatario
    propriatario = utils.ler_string(3,"Introduza o nome do propriatário do veículo: ")

    # introduzir a matricula do carro
    matricula = utils.ler_string(8,"Introduza a matricula do veículo (aa-bb-cc): ")
    if "-" not in matricula:
        print("Matricula invalida!")
        return

    # introduzir a marca do carro ou modelo
    modelo = utils.ler_string(4,"Introduza a marca/modelo do veículo: ")

    # introduzir oque deseja fazer na oficina
    pecas_usar = utils.ler_string(3,"Introduza as reparações que deseja fazer (Troca de óleo, Pintura, Revisão geral): ")
    # variavel fica a none caso o utilizador não pedir para fazer pintura
    cor = None
    if "pintura" in pecas_usar:
            cor = utils.ler_string(3,"indique a cor que deseja: ")
    # separar as opções
    if "," in pecas_usar:
        pecas_usar = pecas_usar.lower().split(",")

    # criar o novo dicionario
    novo = {
        "matricula":matricula,
        "modelo": modelo,
        "propriatario": propriatario,
        "estado" : "em espera",
        "peças" : pecas_usar,
        "cor_mudar" : cor}
    
    # colocar o novo dicionario na lista dos carros
    carros.append(novo)
    print(f"Veículo registrado com sucesso.")

def Editar():
    """Função responsável por editar a ficha dos carros"""
    # Pesquisar a ficha a editar
    ficha_editar = Pesquisar() 
    # escolher o campo a editar
    lista_campos = list(ficha_editar.keys())
    # remover os campos privados
    for c in lista_campos_privados:
        lista_campos.remove(c)
    op = utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo = lista_campos[op-1]
    # mostrar o valor atual do campo a editar
    print(f"O campo {campo} tem o seguinte valor {ficha_editar[campo]}")
    novo_valor = utils.ler_string(3,"Novo valor: ")
    # guardar o novo valor
    ficha_editar[campo] = novo_valor
    print(ficha_editar,carros)
    print("Edição concluída com sucesso.")

def Apagar():
    """Função responsável por apagar a ficha dos carros"""

def Listar():
    """Função responsável por listar a ficha dos carros registrados"""

def Pesquisar():
    """Devolver a lista dos carros que correspondem a um campo"""
    # Deixar o utilizador escolher o campo de pesquisa
    op = utils.Menu(["Modelo","Matricula","Propriatário"],"Escolha o campo de pesquisa:")
    if op == 1:
        campo = "modelo"
    elif op == 2:
        campo = "matricula"
    else:
        campo = "propriatario"
    pesquisa = utils.ler_string(3,f"{campo} a pesquisar: ")
    # Adicionar à lista os carros que correspondem ao resultado da pesquisa
    for carro in carros:
        if pesquisa.lower() in carro[campo].lower():
            op = utils.ler_string(1,f"O carro é o {carro["modelo"]} do senhor/a {carro["propriatario"]}? s/n: ")
            if op in "sS":
                return carro