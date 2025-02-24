"""
Pretendemos criar um sistema de recomendações para compras
Para isso devemos recomendar produtos que o joão ainda não comprou
mas que pertencem a uma categoria de produtos que já tenha
"""
# compras do joão
joao = {"tv","sapatos","tablet"}
# Produtos de categoria
roupa = {"calções","casaco","tshirt"}
calcado = {"sapatos","botas","sapatilhas"}
eletronica = {"tv","tablet","pc","xbox"}

# recomendar produtos cuja categoria pertence a um produto que o joão ja comprou mas cujo produto ainda não comprou

# testar se ja comprou roupa
joao_roupa = joao.intersection(roupa)
if len(joao_roupa) > 0:
    # os produtos de roupa que o joão ainda não comprou
    roupa_para_joao = roupa.difference(joao)
    print(f"Recomendamos comprar {roupa_para_joao}")

# testar se ja comprou calçado
joao_calcado = joao.intersection(calcado)
if len(joao_calcado) > 0:
    # os produtos de calçado que o joão ainda não comprou
    calcado_para_joao = calcado.difference(joao)
    print(f"Recomendamos comprar {calcado_para_joao}")

# testar se ja comprou eletronicos
joao_eletronica = joao.intersection(eletronica)
if len(joao_eletronica) > 0:
    # os produtos de eletronicos que o joão ainda não comprou
    eletronica_para_joao = eletronica.difference(joao)
    print(f"Recomendamos comprar {eletronica_para_joao}")