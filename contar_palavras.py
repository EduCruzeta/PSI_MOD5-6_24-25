""" Ler do utilizador uma frase e contar quantas palavras únicas tem a frase"""
# ler o texto do utilizador
texto = input("Insira a frase: ")
# lista das palavras
texto = texto.strip().split(" ")
# converter lista em sets
conjunto = set(texto)
# len para contar
print(len(conjunto))