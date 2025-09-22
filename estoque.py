
import produto as produto_model

def dar_entrada_estoque(id_produto, quantidade):
    if quantidade <= 0:
        return "Erro: A quantidade deve ser um número positivo."
        
    produto = produto_model.buscar_produto_por_id(id_produto)
    if produto:
        produto['estoque'] += quantidade
        return f"Entrada de {quantidade} unidades para o produto '{produto['nome']}' realizada. Novo estoque: {produto['estoque']}"
    return "Erro: Produto não encontrado."