"""
Trabalho gestao da oficina - Módulo 6
-------------------------------------------------
Um programa para gerir uma oficina 
    - Gestão dos carros (CRUD)
    - Gestão da oficina (listar os status dos carros, peças usadas na manutenção, pesquisar por um carro em especifico)
"""
import utils, os, fichas_clientes, oficina

# Função responsavel pelo menu principal
def MenuPrincipal():
    op = 0
    while op != 3:
        os.system("cls")
        op = utils.Menu(["Ficha cliente","Oficina"],"Menu Principal")
        if op == 3:                 
            break
        if op == 1:
            fichas_clientes.MenuClientes()
        if op == 2:
            oficina.MenuOficina()

if __name__=="__main__":
    MenuPrincipal()
