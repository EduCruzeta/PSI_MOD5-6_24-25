#Desafio mod-5

#desafio 1
notas = {"aluno1":{"pt":0,"ing":0,"ai":0,"tic":0},"aluno2":{"pt":0,"ing":0,"ai":0,"tic":0}}

for chave in notas:
    soma = 0
    for disciplina in notas[chave]:
        nota = int(input(f"Insira a nota de {disciplina} de {chave}: "))
        notas[chave][disciplina] = nota
        soma = soma + nota
    media = soma/4
    notas[chave]["media"] = media
    print(f"A media do aluno {chave} foi de {media}.")

media_total =(notas["aluno1"]["media"] + notas["aluno2"]["media"])/2

print(media_total)

for aluno in notas:
    print(aluno)
    for disciplina in notas[aluno]:
        print(disciplina,notas[aluno][disciplina])


#desafio 2

for cliente in dicionario:
    print(cliente)
    for visitas in dicionario[cliente]:
        print(f"{visitas} - {dicionario[cliente][visitas]}")

codigo = int(input("codigo"))
print(dicionario[codigo]["visitas"])

codigo = int(inpit("codigo visitante"))
dicionario[codigo]["visitaws"] += 1

maior = 0
cidade_maior = 0

for chave in dicionario:
    t_cidade = dicionario[chave]["cidade"]
    nr_visitas = dicionario[chave]["visitas"]
    for codigo in dicionario:
        if t_cidade == dicionario[codigo]["cidade"]:
            nr_visitas = dicionario[codigo]["visitas"]

if nr_visitas > maior:
    cidade_maior = t_cidade
    maior = nr_visitas

