"""O programa vai fazer de cicionario real com as seguintes opções:
Ex: 1. Adicionar defenição
    2. Listar Todas as Defenições
    3. Pesquisar Defenições
    4. Apagar
    5. Terminar"""

from dicionario import Adicionar,Listar,Pesquisar,Apagar

def Menu():
    dicionario = {}
    print("1. Adicionar defenição\n2. Listar Todas as Defenições\n3. Pesquisar Defenições\n4. Apagar\n5. Terminar")
    op = 0
    while op != 5:
        op = int(input("Opção: "))
        if op == 1:
            Adicionar(dicionario)
        elif op == 2:
            Listar(dicionario)
        elif op == 3:
            Pesquisar(dicionario)
        elif op == 4:
            Apagar(dicionario)

Menu()