from . import db
class Produto(db.Model):
    
    __tablename__ = 'produtos'
    
    produto_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    produto_nome = db.Column(db.String(100), nullable=False)
    produto_preco = db.Column(db.Numeric(10,2), nullable=False)
    
