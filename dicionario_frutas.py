"""O programa vai ler o nome da fruta e a quantidade delas"""

mercadoria = {}

for i in range(10):
    fruta = input("Insira a fruta que deseja adicionar: ")
    mercadoria[fruta] = int(input(f"Insira a quantidade de {fruta}: "))

fruta_naogosta = input("insira a fruta que nao gosta: ")
del mercadoria[fruta_naogosta]

print(mercadoria)