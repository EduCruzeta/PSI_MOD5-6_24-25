"""
Programa para gerir o stock de produtos. 
De cada vez que um produto é vendido o stock deve baixar e de cada 
vez que o produto é comprado o stock aumenta

exemplo:
    vender 10 bananas - diminui o stock das batatas em 10
    comprar 50 bananas - aumenta o stock das bananas em 50
    terminar - termina o programa
Se for inserido um comando nao conhecido deve ser apresentada uma mensagem de erros
De cada vez que é realizada uma operação deve ser indicado o stock remanescente incluindo a unidade de medida
Não deve ser possivel vender stock que não existe e não deve ser possível comprar valores negativos de stocks
"""
produtos = ["batatas","bananas","arroz"   ,"bacalhau","maças" ]
stock    = [10       , 50     , 10        , 5        , 5      ] 
unidades = ["kg"     ,"kg"    ,"embalagem","unidade" ,"kg"    ]

def Existe(produto):
    if produto not in produtos:
        print("O produto não existe")
        return False
    return True

def Vender(produto,quantidade):
    """ Recebe o produto e a quantidade a vender, atualiza e mostra o stock"""
    if Existe(produto) == False:
        return
    quantidade = int(quantidade)
    posicao = produtos.index(produto)
    quantidade_stock = stock[posicao]
    if quantidade_stock < quantidade:
        print("Não existe quantidade suficiente disponível.")
        return
    stock[posicao] -= quantidade
    print(f"Venda registrada com sucesso. Ficou com {stock[posicao]}{unidades[posicao]} de {produto}.")

def Comprar(produto,quantidade):
    """ Recebe o produto e a quantidade comprar, atualiza o stock e mostra o stock atualizado"""
    if Existe(produto) == False:
        op = input("Pretende adicionar este produto?: ")
        if op in "sS":
            produtos.append(produto)
            stock.append(int(quantidade))
            unidades.append(input("Qual a unidade de medida: "))
        return
    quantidade = int(quantidade)
    posicao = produtos.index(produto)
    stock[posicao] += quantidade
    print(f"Tem {stock[posicao]}{unidades[posicao]} de {produtos[posicao]} em stock")

def Consultar(produto):
    """ Recebe o produto e mostra a quantidade em stock"""
    if Existe(produto) == False:
        return
    posicao = produtos.index(produto)
    print(f"Tem {stock[posicao]}{unidades[posicao]} de {produtos[posicao]} em stock.")
    
def Comando(texto):
    """ Recebe o texto inserido e devolve um tuplo com o comando a quantidade e o produto
        Devolve false quando o comando é terminar
    """
    texto = texto.lower().strip()
    if len(texto) == 0:
        return True
    if texto == "terminar":
        return False
    partes = texto.split(" ")
    if len(partes) < 2 or len(partes) > 3:
        print("Comando não é valido")
        return True
    if partes[0] not in ("vender","comprar","consultar"):
        print("Comando não valido")
        return True
    if partes[0] == "consultar":
        Consultar(partes[1])
    if partes[0] == "vender":
        # comando necessita de 3 partes e a segunda tem de ser um nº
        if (len(partes) != 3) or partes[1].isdigit()==False:
            print("Comando não valido")
            return True
        Vender(partes[2],partes[1])
    if partes[0] == "comprar":
        # comando necessita de 3 partes e a segunda tem de ser um nº
        if (len(partes) != 3) or partes[1].isdigit()==False:
            print("Comando não valido")
            return True
        Comprar(partes[2],partes[1])

def main():
    """ Ciclo do programa inicial"""
    linha = input("introduza um comando: ")
    while Comando(linha) != False:
        linha = input("Introduza um comando: ")
   

if __name__ == "__main__":
    main()






