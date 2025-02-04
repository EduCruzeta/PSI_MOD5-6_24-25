""" O programa vai ler os seguintes dados e inserir em um dicionario nome,morada,codigo postal,idade,pai,mae,casado
,nr_filhos(nome_1,nome_2)"""

cidadao = {}

def ler_dados(cidadao):
    # Cria a chave e le o valor
    cidadao["nome"] = input("insira o nome: ")
    cidadao["morada"] = input("insira a morada: ")
    cidadao["Codigo postal"] = input("insira o codigo postal: ")
    cidadao["idade"] = int(input("insira a sua idade: "))
    cidadao["Pai"] = input("insira o nome do seu Pai: ")
    cidadao["Mae"] = input("insira o nome da sua Mãe: ")
    op = input("Casado (s/n)")
    if op == "s":
        cidadao["casado"] = True
    else:
        cidadao["casado"] = False
    cidadao["Nr_filhos"] = input("insira o numero de filhos: ")
    filhos= {}
    for filho in range(cidadao["Nr_filhos"]):
        chave = f"nome_{filho+1}"
        filhos[chave] = input(f"Introduza o nome do filho nº{filho+1}")
    print(filhos)
    cidadao["filhos"] = filhos

ler_dados(cidadao)
print(cidadao)

# mostrar o nome do primeiro filho
print(cidadao["filhos"]["nome_1"])
