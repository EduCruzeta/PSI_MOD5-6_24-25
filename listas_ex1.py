"""
Programa para ler as marcas de carros de um stander. 
O programa deve mostrar qual a marca com mais veiculos

- ler do utilizador as marcas e guardar numa lista
- para de ler quando o utilizador inserir uma marca vazia
- calcular para cada marca quantos carros existem
- mostrar a marca com mais carros
"""
carros_stand = []
op = " "
while op != "":
    op = input("insira a marca do carro: ")
    if op != "":
        carros_stand.append(op)


# contar quantos carros existem de cada marca
marcas = set(carros_stand)  # criar um set com as marcas para nao haver repetidas
maior = 0
mmaior = ""
for marca in marcas:
    contar = carros_stand.count(marca)
    if contar > maior:
        mmaior = marca
        maior = contar
    print(f"Tem cerca de {contar} {marca} no stand")

print(f"A marca {mmaior} é a que tem mais veiculos com {maior} carros")

# remover a marva indicada pelo utilizador
remover_marca = input("insira a marca de carro que deseja remover: ")

while remover_marca in carros_stand:
    carros_stand.remove(remover_marca)


print(carros_stand)


