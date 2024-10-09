from flask import Flask
from models import db
from config import Config
from controllers import produto_bp

def criar_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(produto_bp)
    
    return app
    
if __name__ == '__main__':
    app = criar_app()
    app.run(debug=True)