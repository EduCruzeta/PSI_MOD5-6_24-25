"""Um programa que utiliza um dicionario para guardar os professores responsaveis pelas 
salas do torneio tecla e o nº de alunos que cada sala vai ter. As salas são c5, c6, c7, c8 
e o dicionario deve guardar o nome do professor e o nº  de alunos de cada uma"""

dados = {"c5":{"professor":"p1","n_alunos":10, },
         "c6":{"professor":"p2","n_alunos":14, },
         "c7":{"professor":"p3","n_alunos":12, },
         "c8":{"professor":"p4","n_alunos":8}
         }

# ler dados dos professores e alunos por sala
for i in dados:
    professor = input("insira o nome do profesor responsavél: ")
    alunos = int(input("insira o nº de alunos presentes: "))
    # atualizar o nome do professor
    dados[i]["professor"] = professor
    # atualizar o nº de alunos
    dados[i]["n_alunos"] = alunos

for i in dados:
 print(f"A sala {i} tem como responsavél o professor {dados[i]["professor"]} com {dados[i]["n_alunos"]} alunos presentes.")

# adicionar uma sala, um professor e o nº de alunos introduzido pelo utilizador #
#                                  |  |                                         #
#                                  |  |                                         #
#                                  |  |                                         #
#                                 \    /                                        #
#                                  \  /                                         #
#                                   \/                                          #
#                                                                               #                
# pedir o nome da sala nova e do professor e o numero de alunos                 #
salanova = input("insira o nome da nova sala: ")                                #
professor = input("insira o nome do profesor responsavél: ")                    #
alunos = int(input("insira o nº de alunos presentes: "))                        #
                                                                                #
# adicionar ao dicionario a sala nova com os respetivos dados                   #
dados[salanova] = {"professor":professor,"n_alunos":alunos}                     #
                                                                                #
# remover a sala c5 do dicionario                                               #
del dados["c5"]                                                                 #
                                                                                #
print(dados)                                                                    #
#-------------------------------------------------------------------------------#