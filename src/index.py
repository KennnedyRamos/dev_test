from flask import Flask, jsonify, request
from src.config.db import init_db, db
from src.Entity.user import User
from src.Entity.post import Post
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Configurando a URI do banco de dados a partir da variável DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
init_db(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Hello, World!"

# Endpoint para criar um usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(firstName=data['firstName'], lastName=data['lastName'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Endpoint para criar um post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    user = User.query.get(data['userId'])
    if not user:
        return jsonify({'message': 'User not found'}), 404
    new_post = Post(title=data['title'], description=data['description'], userId=data['userId'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

