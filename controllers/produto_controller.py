from flask import Blueprint, request, jsonify
from models import db, Produto

produto_bp = Blueprint('produtos', __name__)

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json
    novo_produto = Produto(produto_nome = data['produto_nome'], produto_preco = data['produto_preco'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'id': novo_produto.produto_id, 'produto_nome': novo_produto.produto_nome, 'produto_preco': novo_produto.produto_preco}), 201

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    lista_produtos = [{'id': produto.produto_id, 'nome': produto.produto_nome, "preço": produto.produto_preco} for produto in produtos]
    return jsonify(lista_produtos)

@produto_bp.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    data = request.json
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    produto.produto_nome = data['produto_nome']
    db.session.commit()
    return jsonify({'id': produto.produto_id, 'nome': produto.produto_nome}), 200

@produto_bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto deletado com sucesso'}), 204