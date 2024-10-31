from sqlalchemy import ForeignKey
from . import db

class Pedido(db.Model):
    
    __tablename__ = 'pedidos'
    
    pedido_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id =db.Column(db.Integer, ForeignKey("clientes.cliente_id"), nullable=False)
    cliente = db.relationship('Cliente', backref='pedidos', lazy='select')
    data_compras = db.Column(db.Date, nullable=False)
    

