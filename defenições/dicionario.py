
def Adicionar(dicionario):
    """Função resposavél por adicionar as palavras e defenições do dicionario"""
    palavra = input("Insira a palavra que deseja inserir: ")
    if palavra not in dicionario.keys():
        dicionario[palavra] = input("Insira a defenição da palavra: ")
    elif palavra in dicionario.keys():
        print("A palavra já esta associada a uma defenição:")
        escolha = input("Deseja alterar s/n: ")
        if escolha in "Ss":
            dicionario[palavra] = input("Insira a nova defenição: ")
        else:
            return

def Listar(dicionario):
    """Função responsavel por mostrar as palavras e as suas respetivas defenições"""
    # Ordenar as chaves
    chaves = dicionario.keys()
    chaves = sorted(chaves)
    for chave in chaves:
        print(f"{chave} -> {dicionario[chave]}")

def Pesquisar(dicionario):
    """Função responsável por pesquisar uma palavra no dicionario e mostra a sua defenição"""
    # ler o termo a pesquisar
    chave_pesquisar = input("Introduza a palavra, ou parte da palavra, a pesquisar: ")
    # precorrer o dicionario
    for chave,valor in dicionario.items():
        # se o termo existir no inicio da chave mostrar o valor
        if chave_pesquisar == chave[:len(chave_pesquisar)]: # slicing para so comprar o inicio da chave
            print(f"{chave} -> {valor}")

def Apagar(dicionario):
    """Função resposável por apagar uma palavra e a sua defenição"""
    # ler o termo a apagar
    chave_apagar = input("Introduza a palavra, ou parte da palavra, a apagar: ")
    # Precorrer o dicionario
    for chave, valor in dicionario.items():
        # se o termo existir no inicio da chave mostrar o valor
        if chave_apagar == chave[:len(chave_apagar)]: # slicing para só comparar o inicio
            print(f"{chave} -> {valor}")
            op = input(f"Pretende remover{chave} do dicionario?: ")
            if op == "s":
                del dicionario[chave]
                return # uma vez que o dicionario foi alterado não podes continuar o ciclo
