alunos = [
    {"nprocesso":123,"nome":"maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"antónio","email":"antonio@gmail.com"}
]

notas = [
    {"nprocesso":alunos[0],"notas":[10,11,12,13]},
    {"nprocesso":alunos[1],"notas":[10,15,8,14]}
]

# Mostrar o nome e as notas dos alunos os alunos sem nota não devem aparecer

for nota in notas:
    print(f"{nota["nprocesso"]["nome"]} - {nota["notas"]}")

# apagar o primeiro aluno

del alunos[0]

for nota in notas:
    print(f"{nota["nprocesso"]["nome"]} - {nota["notas"]}")

print(alunos)