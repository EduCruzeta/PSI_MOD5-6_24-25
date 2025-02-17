import numpy as np
notas = np.array ([12,10,11,14])

aluno1 = {"nome":"joaquim","turma":"10T","email":"joaquim@gmail.com","notas":notas}

# listar as notas do aluno 1
for nota in aluno1["notas"]:
    print(nota)