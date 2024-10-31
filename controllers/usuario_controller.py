from flask import Blueprint, request, jsonify
from models import Usuario 
from models import db 

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuario', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_usuario = Usuario(usuario_nome = data['usuario_nome'], senha = data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'id': novo_usuario.usuario_id, 'nome': novo_usuario.usuario_nome}), 201

@usuario_bp.route('/usuario', methods=['GET'])
def listar_usuario():
    usuarios = Usuario.query.all()
    list_usuarios = [{'usuario_id': u.usuario_id, 'usuario_nome': u.usuario_nome} for u in usuarios]
    return jsonify(list_usuarios)

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario não encontrado'}), 404
    
    usuario.usuario_nome = data['usuario_nome']
    db.session.commit()
    return jsonify({'id': usuario.usuario_id, 'nome': usuario.usuario_nome}), 200

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify({'error': 'Usuario não encontrado'}), 404
    
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario deletado com sucesso'}), 204


    
    