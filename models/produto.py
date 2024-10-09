from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
def __repr__(self):
    return f'<Produto {self.nome}>'