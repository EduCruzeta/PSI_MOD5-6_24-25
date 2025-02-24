"""Um programa que calcula:
-Os alunos que estiveram presentes todos os dias
-Os alunos que faltaram pelo menos 1 dia
-Os alunos que estiveram presentes na segunda e na sexta, mas não estiveram na terça, quarta, quinta
"""

# conjunto com os alunos presentes em cada dia da semana
segunda = {"Ana","Carlos","Pedro","Maria"}
terca = {"Ana","João","Pedro","Clara"}
quarta = {"Maria","Pedro","Ana","Paulo"}
quinta = {"João","Clara","Paulo","Ana"}
sexta = {"Ana","Maria","Carlos","Paulo"}

conjunto = segunda.union(terca,quarta,quinta,sexta)
# Os alunos que estiveram presentes todos os dias
todos_dias = segunda & terca & quarta & quinta & sexta
print(f"O/A aluno/a presente todos os dias foi o/a : {todos_dias}")

# Os alunos que faltaram pelo menos 1 dia
faltar_1_dia = segunda.union(terca,quarta,quinta,sexta)-todos_dias
print(f"Os alunos que faltaram pelo menos 1 vez foram: {faltar_1_dia}")

# Os alunos que estiveram presentes na segunda e na sexta, mas não estiveram na terça, quarta, quinta
alunos_t_q_q = terca | quarta | quinta # "|" = uniao
alunos_s_sx = segunda & sexta          # "&" = interseção
presentes_s_s = alunos_s_sx - alunos_t_q_q # "-" = diferença
print(f"O/Os aluno/s presentes na segunda e na sexta foram: {presentes_s_s}")