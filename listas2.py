cores = []

# adicionar a cor vermelho
cores.append("vermelho") # adiciona no final da lista
# adicionar uma cor introduzida pelo utilizador 
cor = input("indique a cor: ")
cores.append(cor)
# inserir numa posição
cores.insert(0,"amarelo") # inserir o amarelo na posição 0, os restantes elementos são reorganizados
print(cores)

# remover os itens
cores.remove("vermelho") # remove o primeiro e da erro se não encontrar

cor_removida = cores.pop(0)  #remove o elemento da posição indicada dá erro se a lista estiver vazia ou não existir a posição
print(f"Cor removida {cor_removida}")

carros = ["ford","ferrari","bmw","vw"]
del carros[1:3] # remove os elementos nas posições 1 e 2
print(carros)

# remover todos
carros.clear()

# recriar a lista
carros = []

# listar todos os elementos
for cor in cores:
    print(cor)

for posicao in range(len(cores)):
    print(cores[posicao])