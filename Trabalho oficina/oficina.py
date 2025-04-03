"""
Módulo responsável pela gestão da oficina
"""

import utils, os, fichas_clientes

# lista onde vão ficar os carros que estão na oficina
manutencoes = [{"proprietario":"joão alves","modelo":"Toyota Corolla","matricula":"AA-MM-hh","pecas":"Troca de óleo"}]# tirar o modelo nao vale a pena

def MenuOficina():
    """Submenu para gerir a oficina"""
    os.system("cls")
    op = 0
    while op != 3:
        op = utils.Menu(["Pedir manutenção","Levantar carro","Voltar"],"Menu Carros")
        if op == 3:
            break
        if op == 1:
            PedirManutencao()
        if op == 2:
            LevantarCarro()

def LevantarCarro():
    """Função responsavél para o utilizador levantar o carro"""
    # verificar se tem carros na oficina
    if len(manutencoes) == 0:
        print("Não existem carros de momento na oficina.")
        return

    # listar todos os carros em manutenção
    listar = 1
    for carro in manutencoes:
        print(f"{listar}- Propriatário: {carro["proprietario"]} Modelo:{carro["modelo"]} | Matricula:{carro["matricula"]} | peças a levar:{carro["pecas"]}")
        listar +=1

    # verificar qual carro vai ser levantado
    op = utils.ler_numero_inteiro_limites(0,len(manutencoes),"Introduza o nº do carro a ser levantado (introduza 0 para voltar): ")
    if op == 0:
        return
    carro = manutencoes[op-1]

    # verificar se é o carro para levantar
    print(f"proprietário: {carro["proprietario"]} | {carro["modelo"]} | matricula: {carro["matricula"]}")
    op = utils.ler_string(1,"Deseja levantar o carro? s/n:")
    if op in "sS":
        # dizer oque foi feito no carro
        print(f"Foram usadas as seguintes peças no seu veiculo:{carro["pecas"]}")
        # mostrar qual o carro a sair
        print(f"Carro a sair: {carro["modelo"]} | proprietário: {carro["proprietario"]}")
        # retirar o carro da lista de manutenções
        manutencoes.remove(carro)
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
        else:
            return
    
    # verificar se tem mais que 1 carro
    if len(ficha["veiculos"]) >= 2:
        # escolher qual dos carros vai para manutenção
        carro = fichas_clientes.PesquisarCarro(ficha)
    else:
        carro = ficha["veiculos"][0]

    # verificar se o carro ja está em manutenção
    for carro_manutencao in manutencoes:
        if carro["matricula"] == carro_manutencao["matricula"]:
            print("O carro ja está em manutenção.")
            return

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
        op = utils.ler_string(1,f"Tem as seguintas peças {set(pecas_usar)} Deseja fazer mais alterações s/n: ")

    # passar a lista para um set para evitar repetições
    pecas_usar = set(pecas_usar)

    # adicionar quais são as peças que utilizou
    carro["pecas"] = pecas_usar

    # adicionar o carro a lista de manutenções
    novo = {"proprietario":ficha["proprietario"],"matricula":carro["matricula"],"modelo":carro["modelo"],"pecas":pecas_usar}
    manutencoes.append(novo)
    print("Registado com sucesso.")
