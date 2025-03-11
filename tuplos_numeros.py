vencimentos = (1000,5000,2500,1350,4750,850)
nomes = ("A","B","C","D","E","F")

# utilizando uma função
"""Calcular e devolver a soma de todos os vencimentos, o maior e o menor"""
def calculos(vencimentos):
    soma =  sum(vencimentos)
    maximo = max(vencimentos)
    minimo = min(vencimentos)
    return (soma,maximo,minimo) # devolve um tuple

# desempacotamento do tuple para variaveis
soma, maximo, minimo = calculos(vencimentos)

print(f"A soma total é {soma} o maior vencimento é {maximo} e o menor é {minimo}")
    
# calcular e mostrar a media dos vencimentos
media = soma/len(vencimentos)

print(f"A media dos vencimentods é {media}")

# mostrar o nome que tem o maior vencimento
posicao = vencimentos.index(maximo)
print(f"O maior vencimento é {vencimentos[posicao]} do senhor(a) {nomes[posicao]}")