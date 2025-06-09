import random

numero = random.randint(1, 100)
chute = int(input("Adivinhe o número: "))

while chute != numero:

    if chute < numero:
        chute = int(input("\n o numero eh maior: "))

    elif chute > numero:
        chute = int(input("É menor: "))

else:
    print("pabens moco")
# while chute != numero:
#     input("Tente denovo: ")

# else:
#     print("Parabéns")