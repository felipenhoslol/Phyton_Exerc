def soma_numeros(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insira o terceiro número: '))
num4 = int(input('Insira o quarto número: '))

soma = soma_numeros(num1, num2, num3, num4)
print(f"\nA soma dos número é: {soma}")