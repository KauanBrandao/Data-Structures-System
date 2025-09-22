

def menuInicial():
    print("\n------- Menu Inicial -------")
    print("1. Gestão de produtos")
    print("2. Controle de estoque")
    print("3. Gestão de fornecedores")
    print("4. Sair")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        return -1 # Retorna um valor inválido

def menuGestaoProdutos():
    print("\n--- Gestão de Produtos ---")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Editar produto")
    print("4. Excluir produto")
    print("5. Voltar ao menu inicial")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        return -1

def menuGestaoEstoque():
    print("\n--- Gestão de Estoque ---")
    print("1. Consultar estoque de um produto")
    print("2. Dar entrada no estoque")
    print("3. Voltar ao menu inicial")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        return -1

def menuGestaoFornecedores():
    print("\n--- Gestão de Fornecedores ---")
    print("1. Cadastrar fornecedor")
    print("2. Listar fornecedores")
    print("3. Editar fornecedor")
    print("4. Excluir fornecedor")
    print("5. Voltar ao menu inicial")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        return -1