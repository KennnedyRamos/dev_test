from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

# Instanciando o banco de dados
db = SQLAlchemy()

def init_db(app):
    # Configurando a URI do banco de dados a partir da variável de ambiente
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    
    # Desabilitando o rastreamento de modificações no SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializando o banco de dados com o app Flask
    db.init_app(app)
