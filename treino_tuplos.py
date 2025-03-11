"""exercicio para treinar o uso dos tuplos"""

meses = "janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"

# Mostar o 3 mes do ano
print(meses[2])

# mostar os meses do verão
meses_verao = meses[5:9]
print(meses_verao)

# verificar se junho esta nos meses do ano
if "junho" in meses_verao:
    print("Junho está presente nos meses de verão")
else:
    print("Junho não faz parte do verão")

# Listar os meses por ordem alfabetica
print(sorted(meses))

# Mostrar os meses cujo nome começa por j
for i in meses:
    if i[0] == "j":
        print(i)

# Mostrar os mes(es) com maior nome
maior = ""
for i in meses:
    if len(i) > len(maior):
        maior = i

print(maior)


