"""
Trabalho gestao da oficina - Módulo 6
-------------------------------------------------
Um programa para gerir uma oficina 
    - Gestão dos carros (CRUD)
    - Gestão da oficina (listar os status dos carros, peças usadas na manutenção, pesquisar por um carro em especifico)
    - Gestão das peças (listar,adicionar,editar,remover peças e verificar stock )
"""
import utils, os, fichas_clientes, oficina, Pecas

# Função responsavel pelo menu principal
def MenuPrincipal():
    op = 0
    fichas_clientes.LerDados()
    Pecas.Ler()
    while op != 4:
        os.system("cls")
        op = utils.Menu(["Ficha cliente","Oficina","Peças","Sair"],"Menu Principal")
        if op == 4:                 
            break
        if op == 1:
            fichas_clientes.MenuClientes()
        if op == 2:
            oficina.MenuOficina()
        if op == 3:
            Pecas.MenuPecas()

if __name__=="__main__":
    MenuPrincipal()
