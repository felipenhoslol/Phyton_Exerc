produtos = []

def adicionar_produto(nome, quantidade):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("Produto já cadastrado.")
            return
    novo_produto = {"nome": nome, "quantidade": quantidade}
    produtos.append(novo_produto)
    print("Produto adicionado com sucesso!")

def buscar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f'Produto encontrado: {produto["nome"]} | Quantidade: {produto["quantidade"]}')
            return produto
    print("Produto não encontrado.")
    return None

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f'Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]}')

def atualizar_estoque(nome, nova_quantidade):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] = nova_quantidade
            print("Estoque atualizado com sucesso!")
            return
    print("Produto não encontrado.")

while True:
    print("\n--- Sistema de Cadastro de Produtos ---")
    print("1. Adicionar produto")
    print("2. Buscar produto")
    print("3. Listar produtos")
    print("4. Atualizar estoque")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        try:
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, quantidade)
        except ValueError:
            print("Quantidade deve ser um número inteiro.")
    elif opcao == '2':
        nome = input("Nome do produto para buscar: ")
        buscar_produto(nome)
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        nome = input("Nome do produto para atualizar: ")
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            atualizar_estoque(nome, nova_quantidade)
        except ValueError:
            print("Quantidade deve ser um número inteiro.")
    elif opcao == '5':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")