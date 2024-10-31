from flask import Blueprint, request, jsonify
from models import db, Cliente 

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/cliente', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_cliente = Cliente(cliente_nome = data['cliente_nome'], cliente_email = data['cliente_email'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'id': novo_cliente.cliente_id, 'cliente_nome': novo_cliente.cliente_nome, 'cliente_email': novo_cliente.cliente_email}), 201

@cliente_bp.route('/cliente', methods=['GET'])
def listar_cliente():
    clientes = Cliente.query.all()
    lista_cliente = [{'id': cliente.cliente_id, 'nome': cliente.cliente_nome, 'email': cliente.cliente_email} for cliente in clientes]
    return jsonify(lista_cliente)

@cliente_bp.route('/cliente/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    data = request.json
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    
    cliente.cliente_email = data['cliente_email']
    db.session.commit()
    return jsonify({'id': cliente.cliente_id, 'nome': cliente.cliente_nome, 'email': cliente.cliente_email}), 200
 
@cliente_bp.route('/cliente/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    cliente = Cliente.query.get(id)
    
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente deletado com sucesso'}), 204