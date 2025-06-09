def informacoes(nome, raca, alinhamento, pts_vida, pts_energ, personalidade):
    return (nome, raca, alinhamento, pts_vida, pts_energ, personalidade)

print("Bem vindo ao jogo Dê e Dê!\n")

nome = input("insira seu nome: ")
raca = input("insira sua raça: ")
alinhamento = input("insira seu alinhamento: ")
pts_vida = input("insira seus pontos de vida: ")
pts_energ = input("insira seus pontos de energia: ")
personalidade = input("insira sua personalidade: ")

resultado = informacoes(nome, raca, alinhamento, pts_vida, pts_energ, personalidade)

print("\n", resultado)

print("\nSeu personagem foi criado com sucesso!")