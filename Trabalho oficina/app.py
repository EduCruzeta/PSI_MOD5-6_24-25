"""
Trabalho gestao da oficina - Módulo 6
-------------------------------------------------
Um programa para gerir uma oficina 
    - Gestão dos carros (CRUD)
    - Gestão da oficina (listar os status dos carros, peças usadas na manutenção, pesquisar por um carro em especifico)
"""
import utils, os, carros, oficina

# Função responsavel pelo menu principal
def MenuPrincipal():
    op = 0
    while op != 4:
        os.system("cls")
        op = utils.Menu(["Carros","Oficina"],"Menu Principal")
        if op == 4:                 
            break
        if op == 1:
            carros.MenuCarros()
        if op == 2:
            oficina.MenuOficina()



if __name__=="__main__":
    MenuPrincipal()
