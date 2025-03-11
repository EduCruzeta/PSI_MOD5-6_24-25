notas = {
    "joaquim" : (10,12,14,8,15),
    "maria" : (14,10,13,8,15),
    "antónio" : (10,11,12,10,11),
}

disciplinas = ("pt","ing","mat","psi","ef")

# calcular e mostrar a media das notas de cada aluno
maior_media = 0
nomemm = ""
for aluno in notas:
    media = sum(notas[aluno]) / len(notas[aluno])
    if media > maior_media:
        maior_media = media
        nomemm = aluno
    print(f" A media do(a) {aluno} é {media}")

# mostrar o nome do aluno com a melhor média
print(f"A maior media é {maior_media} que pertence ao aluno(a) {nomemm}")

# mostrar o nº de negativas de cada aluno
negativas = 0
for aluno in notas:
    negativas = 0
    for nota in notas[aluno]:
        if nota < 10:
            negativas += 1
    # mostar o nome dos aluno sem negativas
    if negativas == 0:
        print(f"O {aluno} não tem negativas")
    else:
        print(f"O {aluno} tem {negativas} negativas")

# calcular e mostrar a média das notas de cada disciplina

for i in range(len(disciplinas)):
    soma = 0
    for aluno in notas:
        soma += notas[aluno][i]
    media = soma / len(notas.keys())
    print(f"A disciplina {disciplinas[i]} tem média de {round(media)}")

# criar um dicionario com o nome do aluno, o nome das diciplinas e as respetivas notas de cada aluno

notas_v2 = {}

for aluno in notas:
    notas_v2[aluno] = {}
    for i in range(len(disciplinas)):
        notas_v2[aluno][disciplinas[i]] = notas[aluno][i]

print(notas_v2)