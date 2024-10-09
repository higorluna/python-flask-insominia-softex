from flask import Blueprint, request, jsonify
from models import db, Produto 

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json
    novo_produto = Produto(nome = data['nome'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'id': novo_produto.id, 'nome': novo_produto.nome}), 201

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    lista_produtos = [{'id': produto.id, 'nome': produto.nome} for produto in produtos]
    return jsonify(lista_produtos)

@produto_bp.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    data = request.json
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    produto.nome = data['nome']
    db.session.commit()
    return jsonify({'id': produto.id, 'nome': produto.nome}), 200

@produto_bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto deletado com sucesso'}), 204