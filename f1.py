'''
PSI - Módulo 6
Coleções - F1
'''
 
GrandePremios = [
    {"Número": 1, "Grande Prémio": "Barém", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 2, "Grande Prémio": "Arábia Saudita", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 3, "Grande Prémio": "Austrália", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número": 4, "Grande Prémio": "Japão", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 5, "Grande Prémio": "China", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 6, "Grande Prémio": "Miami", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 7, "Grande Prémio": "Emília-Romanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 8, "Grande Prémio": "Mônaco", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 9, "Grande Prémio": "Canadá", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 10, "Grande Prémio": "Espanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 11, "Grande Prémio": "Áustria", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 12, "Grande Prémio": "Grã-Bretanha", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 13, "Grande Prémio": "Hungria", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 14, "Grande Prémio": "Bélgica", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 15, "Grande Prémio": "Países Baixos", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 16, "Grande Prémio": "Itália", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 17, "Grande Prémio": "Azerbaijão", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 18, "Grande Prémio": "Singapura", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 19, "Grande Prémio": "Estados Unidos", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 20, "Grande Prémio": "Cidade do México", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número": 21, "Grande Prémio": "São Paulo", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 22, "Grande Prémio": "Las Vegas", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 23, "Grande Prémio": "Catar", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 24, "Grande Prémio": "Abu Dhabi", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"}
]

def Procura(lista,campo,valor,campo_devolver):
    """
    Recebe a lista, o campo e o valor a procurar e o campo que tem o valor a devolver
    Se valor a devolver é None então devolve todos
    """
    lista_a_devolver=[]
    for v in lista:
        if valor == None or v[campo] == valor:
            lista_a_devolver.append(v[campo_devolver])
    return lista_a_devolver

# Quem ganhou o GP do Brasil
vencedor = Procura(GrandePremios,'Grande Prémio','São Paulo','Vencedor')
print(vencedor)
# Quais os grandes prémios que ganhou a Ferrari
gp_ferrari = Procura(GrandePremios,'Equipa','Ferrari','Grande Prémio')
print(gp_ferrari)
# Quais os Grande Prémios que um determinado piloto ganhou (escolha do utilizador)
piloto=input("Qual o piloto:")
gp_piloto = Procura(GrandePremios,'Vencedor',piloto,'Grande Prémio')
print(gp_piloto)
# Lista de vencedores (só aparece uma vez)
vencedores = Procura(GrandePremios,'Vencedor',None,'Vencedor')
print(set(vencedores))
# Lista de equipas que ganharam provas (só aparece uma vez)
equipas = set(Procura(GrandePremios,'Equipa',None,'Equipa'))
print(equipas)
# Mostrar quantos grandes prémios ganhou cada um desses pilotos
#Com a função
for nome in set(vencedores):
    vitorias = vencedores.count(nome)
    print(f"{nome} - {vitorias}")

#lista com nomes dos vencedores
pilotos_vencedores=[]
for gp in GrandePremios:
    pilotos_vencedores.append(gp['Vencedor'])

for nome in set(pilotos_vencedores):
    vitorias = pilotos_vencedores.count(nome)
    print(f"{nome} - {vitorias}")

#substituir um nome de um piloto
nome_a_procurar="Lando Norris"
nome_a_substituir = "Quim Barreiros"

#percorrer a lista
for gp in GrandePremios:
    if gp['Vencedor']==nome_a_procurar:
        gp['Vencedor']=nome_a_substituir