Partido_A = {"A","B","C"}
Partido_B = {"A","K","Y"}
Partido_C = {"A","B","Z","T"}

# listar os elementos repetidos
partido_a_b = Partido_A.intersection(Partido_B)
partido_a_c = Partido_A.intersection(Partido_C)
partido_b_c = Partido_B.intersection(Partido_C)
repetidos_todos = partido_a_b | partido_a_c | partido_b_c
print(f"Os elementos repetidos em pelo menos 2 partidos são: {repetidos_todos}")
# Listar os elemetos repetidos em todos
elementos_reepetidos = Partido_A.intersection(Partido_B)
elementos_reepetidos = Partido_C.intersection(elementos_reepetidos)
print(f"Elementos comuns a todos os partidos: {elementos_reepetidos}")
# ou
elementos_reepetidos_v2 = Partido_A & Partido_B & Partido_C
print(f"Elementos comuns a todos os partidos: {elementos_reepetidos_v2}")

# listar os elemetos de cada partido sem repetidos
print(f"Partido A:{Partido_A.difference(repetidos_todos)}")
print(f"Partido B:{Partido_B.difference(repetidos_todos)}")
print(f"Partido C:{Partido_C.difference(repetidos_todos)}")
