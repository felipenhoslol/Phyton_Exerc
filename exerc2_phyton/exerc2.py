n = int(input("Insira um número: "))

soma = 0
i = 1

while i <= n:
    if i % 2 != 0:
        soma += i
    i += 1

print(f"A soma de todos os números ímpares de 1 até {n} é {soma}.")