from sqlalchemy import ForeignKey
from . import db

class DetalhePedido(db.Model):
    
    __tablename__ = 'detalhes_pedidos'
    
    detalhe_id = db.Column(db.Integer, primary_key=True)
    detalhe_quantidade = db.Column(db.Integer, nullable=False)
    detalhe_preco = db.Column(db.Numeric(10,2), nullable=False)
    detalhe_desconto = db.Column(db.Numeric(10,2))
    
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedidos.pedido_id"), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.produto_id"), nullable=False)
    
    pedido = db.relationship('Pedido', backref='detalhes_pedidos')
    produto = db.relationship('Produto', backref='detalhes_pedidos')
