from flask import Flask, render_template
from db import db
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user



''' Inicializa o app Flask '''
app = Flask(__name__)

app.secret_key = 'chave_secreta_para_sessoes'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


''' Configurações do banco de dados'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

''' Inicializa o SQLAlchemy com a app '''
db.init_app(app)

''' Importa os modelos depois de configurar o db (evita import circular) '''
from modelos import Car, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


''' Cria as tabelas no banco'''
with app.app_context():
    db.create_all()

''' sistema de registro de usuários '''
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])

        if User.query.filter_by(email=email).first():
            return "❌ E-mail já cadastrado."

        novo_user = User(nome=nome, email=email, senha=senha)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')



''' sistema de login/logout '''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "❌ Credenciais inválidas."
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))





@app.route('/cars')
def mostrar_carros():
    carros = Car.query.all()
    return render_template('cars.html', carros=carros)

from flask import request, redirect, url_for

''' sistema de adicionar carros '''
@app.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        preco_dia = float(request.form['preco_dia'])

        novo_carro = Car(marca=marca, modelo=modelo, preco_dia=preco_dia, user_id=current_user.id)
        db.session.add(novo_carro)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('add_car.html')



@app.route('/cars')
def cars():
    carros = Car.query.all()
    return render_template('cars.html', carros=carros)



''' sistema de dashboard '''
@app.route('/dashboard')
@login_required
def dashboard():
    carros = Car.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', carros=carros)

    




if __name__ == '__main__':
    app.run(debug=True)
