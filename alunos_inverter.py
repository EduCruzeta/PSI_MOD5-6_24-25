alunos = ["joaquim","antonio","maria","carlos","carlos"]

converter_alunos = alunos[::-1]
print(converter_alunos)

# Existem repetidos
if len(alunos) != set(alunos):
    print("Repetidos")
