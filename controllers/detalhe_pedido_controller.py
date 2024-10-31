"""from flask import Blueprint, request, jsonify
from models import db, DetalhePedido

detalhe_pedido_bp = Blueprint('detalhes_pedidos', __name__)
#parei aqui
@pedido_bp.route('/pedido', methods=['POST'])
def criar_pedido():
    data = request.json
    novo_pedido = Pedido(cliente_id = data['cliente_id'], data_compras = data['data_compras'])
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'id': novo_pedido.pedido_id, 'cliente': novo_pedido.cliente_id, 'data_compras': novo_pedido.data_compras}), 201

@pedido_bp.route('/pedido', methods=['GET'])
def listar_pedido():
    pedidos = Pedido.query.all()
    lista_pedido = [{'id': pedido.pedido_id, 'nome': pedido.pedido_nome, 'cliente': pedido.cliente_id, 'data': pedido.data_compras} for pedido in pedidos]
    return jsonify(lista_pedido)

@pedido_bp.route('/pedido/<int:id>', methods=['PUT'])
def atualizar_pedido(id):
    data = request.json
    pedido = Pedido.query.get(id)
    if not pedido:
        return jsonify({'error': 'Pedido não encontrado'}), 404
    
    pedido.data_compras = data['data_compras']
    db.session.commit()
    return jsonify({'id': pedido.pedido_id, 'cliente': pedido.cliente_id, 'data': pedido.data_compras}), 200
 
@pedido_bp.route('/pedido/<int:id>', methods=['DELETE'])
def deletar_pedido(id):
    pedido = Pedido.query.get(id)
    
    if not pedido:
        return jsonify({'error': 'Pedido não encontrado'}), 404
    
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'message': 'Pedido deletado com sucesso'}), 204
    """