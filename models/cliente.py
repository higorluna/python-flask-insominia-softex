from . import db

class Cliente(db.Model):
    
    __tablename__ = 'clientes'
    
    cliente_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_nome = db.Column(db.String(255), nullable=False)
    cliente_email = db.Column(db.String(255), unique=True, nullable=False)
    

