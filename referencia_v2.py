alunos = [
    {"nprocesso":123,"nome":"maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"antónio","email":"antonio@gmail.com"}
]

notas = [
    {"nprocesso":123,"notas":[10,11,12,13]},
    {"nprocesso":124,"notas":[10,15,8,14]}
]

# Mostrar o nome e as notas dos alunos os alunos sem nota não devem aparecer

"""
considereções:
    - O que deve acontecer se tentar apagar o aluno 124? Apagar também as notas ou não deixar apagar o aluno?
    - Posso adicioanr as notas do aluno 129?
    - Não devemos alterar o nprocesso
"""
for aluno in alunos:
    # precorrer os alunos para encontrar o nprocesso correspondente
    for nota in notas:
        # precorrer as notas
        if nota["nprocesso"] == aluno["nprocesso"]:
            print(f"{aluno["nome"]} - {nota["notas"]}")
