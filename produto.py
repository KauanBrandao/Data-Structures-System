

import bancoInMemory as db


def cadastrar_produto(nome, preco, estoque):
    if preco < 0 or estoque < 0:
        return "Erro: Preço e estoque não podem ser negativos."

    novo_id = db.gerar_novo_id_produto()
    novo_produto = {
        'id': novo_id,
        'nome': nome,
        'preco': float(preco),
        'estoque': int(estoque)
    }
    db.PRODUTOS.append(novo_produto)
    return f"Produto '{nome}' cadastrado com sucesso com o ID {novo_id}!"

def listar_produtos():
    return db.PRODUTOS

def buscar_produto_por_id(id_produto):
    for produto in db.PRODUTOS:
        if produto['id'] == id_produto:
            return produto
    return None # Retorna None se não encontrar

def excluir_produto(id_produto):
    produto_para_excluir = buscar_produto_por_id(id_produto)
    if produto_para_excluir:
        db.PRODUTOS.remove(produto_para_excluir)
        return "Produto excluído com sucesso."
    return "Erro: Produto não encontrado."

def editar_produto(id_produto, novo_nome, novo_preco):
    produto_para_editar = buscar_produto_por_id(id_produto)
    if produto_para_editar:
        if novo_preco < 0:
            return "Erro: O novo preço não pode ser negativo."
        produto_para_editar['nome'] = novo_nome
        produto_para_editar['preco'] = float(novo_preco)
        return "Produto atualizado com sucesso!"
    return "Erro: Produto não encontrado com o ID fornecido."

def buscar_produtos_por_nome(nome_parcial):
    produtos_encontrados = []
    termo_busca = nome_parcial.lower()
    for produto in db.PRODUTOS:
        if termo_busca in produto['nome'].lower():
            produtos_encontrados.append(produto)
    return produtos_encontrados