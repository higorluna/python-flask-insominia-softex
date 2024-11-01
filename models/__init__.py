from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cliente import Cliente
from .pedido import Pedido
from .produto import Produto
from .usuario import Usuario
from .detalhePedido import DetalhePedido