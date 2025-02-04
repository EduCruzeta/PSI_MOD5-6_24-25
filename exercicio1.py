"""
Um programa para mostrar a capital de um país introduzido pelo utilizador
"""
capitais = {"Portugual" : "Lisboa",
            "Espanha" : "Madrid",
            "França" : "Paris",
            "Brasil" : "Brasilia",
            "Inglaterra" : "Londres",
             "Itália" : "Roma" }

# Perguntar ao utilizador o pais
pais = input("Insira o país que deseja saber a capital: ")
if pais not in capitais:
    print("Não tenho informações sobre esse país.")
else:
    # mostar a capital desse país
    print(capitais[pais])

# Utilixar a função get - Devolve o valor da chave ou um valor por omissão no caso da chave não existir
print(capitais.get(pais,"Não tenho informações sobre esse país."))



