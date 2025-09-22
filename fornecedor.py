import bancoInMemory as db


def cadastrar_fornecedor(nome, telefone):
    novo_id = db.gerar_novo_id_fornecedor()
    novo_fornecedor = {
        'id': novo_id,
        'nome': nome,
        'telefone': telefone
    }
    db.FORNECEDORES.append(novo_fornecedor)
    return f"Fornecedor '{nome}' cadastrado com sucesso com o ID {novo_id}!"

def listar_fornecedores():
    return db.FORNECEDORES

def buscar_fornecedor_por_id(id_fornecedor):
    for fornecedor in db.FORNECEDORES:
        if fornecedor['id'] == id_fornecedor:
            return fornecedor
    return None

def editar_fornecedor(id_fornecedor, novo_nome, novo_telefone):
    fornecedor_para_editar = buscar_fornecedor_por_id(id_fornecedor)
    if fornecedor_para_editar:
        fornecedor_para_editar['nome'] = novo_nome
        fornecedor_para_editar['telefone'] = novo_telefone
        return "Fornecedor atualizado com sucesso!"
    return "Erro: Fornecedor não encontrado com o ID fornecido."

def excluir_fornecedor(id_fornecedor):
    fornecedor_para_excluir = buscar_fornecedor_por_id(id_fornecedor)
    if fornecedor_para_excluir:
        db.FORNECEDORES.remove(fornecedor_para_excluir)
        return "Fornecedor excluído com sucesso."
    return "Erro: Fornecedor não encontrado."