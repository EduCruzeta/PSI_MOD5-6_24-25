"""O programa vai ler o nome da fruta e a quantidade delas"""

mercadoria = {}

for i in range(2):
    fruta = input("Insira a fruta que deseja adicionar: ") # Pedir a fruta que ele quer adicionar
    mercadoria[fruta] = int(input(f"Insira a quantidade de {fruta}: ")) # Adicionar a quantidade de fruta 

fruta_naogosta = input("insira a fruta que nao gosta: ") # Pedir a fruta que ele não gosta
if fruta_naogosta in mercadoria: # Verificar se a fruta está ou não no dicionario
    del mercadoria[fruta_naogosta] # retirar essa fruta do dicionario
else:
    print("A fruta não esta no dicionario.")

# Listar frutas no dicionario

for chave,valor in mercadoria.items():
    print(f"{chave} -> {valor}")

# Mostrar o nome da fruta com maior quantidade

maior = 0
maior_fruta=""
for chave, valor in mercadoria.items():
    if valor > maior:
        maior = valor
        maior_fruta = chave  
print(f"A fruta com mais quantidade é {maior_fruta} com {maior} elementos.")
