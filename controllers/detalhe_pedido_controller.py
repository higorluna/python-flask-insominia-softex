from flask import Blueprint, request, jsonify
from models import db, DetalhePedido

detalhe_pedido_bp = Blueprint('detalhes_pedidos', __name__)

@detalhe_pedido_bp.route('/detalhe-pedido', methods=['POST'])
def criar_detalhe_pedido():
    data = request.json
    novo_detalhe_pedido = DetalhePedido(detalhe_quantidade = data['detalhe_quantidade'], detalhe_preco = data['detalhe_preco'], detalhe_desconto = data['detalhe_desconto'], pedido_id = data['pedido_id'], produto_id = data['produto_id'])
    db.session.add(novo_detalhe_pedido)
    db.session.commit()
    return jsonify({'id': novo_detalhe_pedido.detalhe_id, 'pedido': novo_detalhe_pedido.pedido_id, 'produto': novo_detalhe_pedido.produto_id}), 201

@detalhe_pedido_bp.route('/detalhe-pedido', methods=['GET'])
def listar_detalhe_pedido():
    detalhes_pedidos = DetalhePedido.query.all()
    lista_detalhes_pedido = [{'id': detalhe_pedido.detalhe_id, 'quantidade': detalhe_pedido.detalhe_quantidade, 'preco': detalhe_pedido.detalhe_preco, 'desconto': detalhe_pedido.detalhe_desconto, 'pedido': detalhe_pedido.pedido_id, 'produto': detalhe_pedido.produto_id} for detalhe_pedido in detalhes_pedidos]
    return jsonify(lista_detalhes_pedido)

@detalhe_pedido_bp.route('/detalhe-pedido/<int:id>', methods=['PUT'])
def atualizar_detalhe_pedido(id):
    data = request.json
    detalhe_pedido = DetalhePedido.query.get(id)
    if not detalhe_pedido:
        return jsonify({'error': 'Detalhe do pedido não encontrado'}), 404
    
    detalhe_pedido.datalhe_desconto = data.get('datalhe_desconto')
    db.session.commit()
    return jsonify({'id': detalhe_pedido.detalhe_id, 'desconto': detalhe_pedido.detalhe_desconto}), 200
 
@detalhe_pedido_bp.route('/detalhe-pedido/<int:id>', methods=['DELETE'])
def deletar_detalhe_pedido(id):
    detalhe_pedido = DetalhePedido.query.get(id)
    
    if not detalhe_pedido:
        return jsonify({'error': 'Detalhe do pedido não encontrado'}), 404
    
    db.session.delete(detalhe_pedido)
    db.session.commit()
    return jsonify({'message': 'Detalhe do Pedido deletado com sucesso'}), 204
    