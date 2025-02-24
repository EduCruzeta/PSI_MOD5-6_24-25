""" 
Calcular o indice de jaccard entre duas frases
"""



frase_a = input("insira a frase A: ")
frase_b = input("insira a frase B: ")

frase_a = frase_a.strip().lower().split(" ")
frase_b = frase_b.strip().lower().split(" ")

conjunto_a = set(frase_a)
conjunto_b = set(frase_b)

resultado = (len(conjunto_a.intersection(conjunto_b))) / (len(conjunto_a.union(conjunto_b)))
print(resultado)