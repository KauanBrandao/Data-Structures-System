import menus
import produto as produto_model
import fornecedor as fornecedor_model
import estoque as estoque_model


def gerenciar_produtos():
    while True:
        escolha = menus.menuGestaoProdutos()
        if escolha == 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço: "))
            estoque_inicial = int(input("Digite o estoque inicial: "))
            print(produto_model.cadastrar_produto(nome, preco, estoque_inicial))
        elif escolha == 2:
            print("\n--- Lista de Produtos ---")
            produtos = produto_model.listar_produtos()
            if not produtos:
                print("Nenhum produto cadastrado.")
            for p in produtos:
                print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")
        elif escolha == 3:
            id_prod = int(input("Digite o ID do produto a editar: "))
            novo_nome = input("Digite o novo nome: ")
            novo_preco = float(input("Digite o novo preço: "))
            print(produto_model.editar_produto(id_prod, novo_nome, novo_preco))
        elif escolha == 4:
            id_prod = int(input("Digite o ID do produto a excluir: "))
            print(produto_model.excluir_produto(id_prod))
        elif escolha == 5:
            break
        else:
            print("Opção inválida!")
        input("\nPressione Enter para continuar...")

def gerenciar_estoque():
    while True:
        escolha = menus.menuGestaoEstoque()
        if escolha == 1:
            nome_busca = input("Digite o nome ou parte do nome do produto: ")
            resultados = produto_model.buscar_produtos_por_nome(nome_busca)
            if not resultados:
                print(f"Nenhum produto encontrado com o termo '{nome_busca}'.")
            else:
                for p in resultados:
                    print(f"-> Nome: {p['nome']} | Estoque: {p['estoque']} unidades")
        elif escolha == 2:
            id_prod = int(input("Digite o ID do produto para dar entrada: "))
            qtd = int(input("Digite a quantidade de entrada: "))
            print(estoque_model.dar_entrada_estoque(id_prod, qtd))
        elif escolha == 3:
            break
        else:
            print("Opção inválida!")
        input("\nPressione Enter para continuar...")


def gerenciar_fornecedores():
    while True:
        escolha = menus.menuGestaoFornecedores()
        if escolha == 1:
            nome = input("Digite o nome do fornecedor: ")
            tel = input("Digite o telefone: ")
            print(fornecedor_model.cadastrar_fornecedor(nome, tel))
        elif escolha == 2:
            print("\n--- Lista de Fornecedores ---")
            fornecedores = fornecedor_model.listar_fornecedores()
            if not fornecedores:
                print("Nenhum fornecedor cadastrado.")
            for f in fornecedores:
                print(f"ID: {f['id']} | Nome: {f['nome']} | Telefone: {f['telefone']}")
        elif escolha == 3:
            id_forn = int(input("Digite o ID do fornecedor a editar: "))
            novo_nome = input("Digite o novo nome: ")
            novo_tel = input("Digite o novo telefone: ")
            print(fornecedor_model.editar_fornecedor(id_forn, novo_nome, novo_tel))
        elif escolha == 4:
            id_forn = int(input("Digite o ID do fornecedor a excluir: "))
            print(fornecedor_model.excluir_fornecedor(id_forn))
        elif escolha == 5:
            break
        else:
            print("Opção inválida!")
        input("\nPressione Enter para continuar...")

def main():
    while True:
        escolha = menus.menuInicial()
        if escolha == 1:
            gerenciar_produtos()
        elif escolha == 2:
            gerenciar_estoque()
        elif escolha == 3:
            gerenciar_fornecedores()
        elif escolha == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


main()