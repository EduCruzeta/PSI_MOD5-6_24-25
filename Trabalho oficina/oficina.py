"""
Módulo responsável pela gestão da oficina
"""

import utils, os, fichas_clientes

# lista onde vão ficar os carros que estão na oficina
manutencoes = []

def MenuOficina():
    """Submenu para gerir a oficina"""
    os.system("cls")
    op = 0
    while op != 4:
        op = utils.Menu(["Pedir manutenção","Levantar carro","Voltar"],"Menu Carros")
        if op == 4:
            break
        if op == 1:
            PedirManutencao()
        if op == 2:
            LevantarCarro()

def LevantarCarro():
    """Função responsavél para o utilizador pode levantar o carro"""
    # verificar se tem carros na oficina
    if len(manutencoes) == 0:
        print("Não existem carro de momento na oficina.")

    # listar todos os carros em manutenção
    for carro in manutencoes:
        print(f"Propriatário:{manutencoes["propriatario"]} | Modelo:{manutencoes["modelo"]} | Matricula:{manutencoes["matricula"]} | peças a levar:{manutencoes["pecas"]}")

    # verificar qual carro vai ser levantado
    op =

    # verificar se o carro está em manutenção
    if carro["estado"] == "Em manutencao":
        op = utils.ler_string(1,"Deseja levantar o carro? s/n:")
        if op in "sS":
            # dizer oque foi feito no carro
            print(f"Foram usadas as seguintes peças no seu veiculo:{carro["pecas"]}")
            # mudar o estado do carro para Pronto a levantar
            carro["estado"] == "Pronto"
            print(f"Carro a sair {carro["modelo"]} | propeiatário {manutencoes["propriatario"]}")
            print("Obrigado por confiar em nós volte sempre.")

def PedirManutencao():
    """Função para o utilizador pedir oque deseja fazer no carro"""
    # pesquisar a ficha do cliente que vai entrar em manutenção
    ficha = fichas_clientes.PesquisarFicha()

    # verificar se o cliente tem ficha
    if ficha == None:
        op = utils.ler_string(1,"Nenhuma ficha encontrada deseja criar uma ficha? s/n")
        if op in "sS":
            fichas_clientes.Adicionar()
            return
    
    # verificar se tem mais que 1 carro
    if len(ficha["veiculos"]) >= 2:
        # escolher qual dos carros vai para manutenção
        carro = fichas_clientes.PesquisarCarro(ficha)
    else:
        carro = ficha["veiculos"][0]

    # perguntar oque vai fazer na oficina   
    op = "s"
    pecas_usar = []
    while op in "sS":
        # introduzir oque deseja fazer na oficina
        escolha = utils.Menu(["Troca de óleo","Revisão geral","Troca de pneus"],"Escolha: ")
        if escolha == 1:
            pecas_usar.append("Troca de óleo")
        if escolha == 2:
            pecas_usar.append("Revisão geral")
        if escolha == 3:
            pecas_usar.append("Troca de pneus")
        # verificar se quer fazer mais alterações
        op = utils.ler_string(1,"Deseja fazer mais alterações s/n: ")

    # adicionar quais são as peças que utilizou
    carro["pecas"] = pecas_usar

    # adicioar o carro a lista de manutenções
    novo = {"propriatario":ficha["propriatario"],"modelo":carro["modelo"],"matricula":carro["matricula"],"pecas":carro["pecas"]}
    manutencoes.append(novo)

    # alterar o estado do carro
    carro["estado"] = "Em manutenção"
    print("Registado com sucesso.")