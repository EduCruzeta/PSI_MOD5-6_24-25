import random
sequencia1 = " "
sequencia2 = ""
contar = 0

while sequencia1!=sequencia2:
    sequencia1 = " "
    sequencia2 = ""
    numeros = [*range(1,13)]
    for i in range(5):
        x = random.choice(numeros)
        numeros.remove(x)
        sequencia1 += str(x)

    numeros1 = [*range(1,13)]
    for i in range(5):
        k = random.choice(numeros1)
        numeros1.remove(k)
        sequencia2 += str(k)
    contar +=1

print(contar)