
from db import db
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime





''' Inicializa o app Flask '''
app = Flask(__name__)

app.secret_key = 'chave_secreta_para_sessoes'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



import os

''' caminho base do projeto '''
basedir = os.path.abspath(os.path.dirname(__file__))

# Detecta se existe variável de ambiente (Railway/Postgres)
database_url = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'instance', 'database.db'))

# Ajuste necessário para o SQLAlchemy aceitar URLs do Postgres
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



''' Inicializa o SQLAlchemy com a app '''
db.init_app(app)

''' Importa os modelos depois de configurar o db (evita import circular) '''
from car_rental_app.modelos import Car, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


''' Cria as tabelas no banco'''
with app.app_context():
    db.create_all()


@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}

''' sistema de registro de usuários '''


@app.route('/')
def home():
    return render_template('index.html')


''' sistema de registro de usuários '''
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_hash = generate_password_hash(request.form['senha'])

        if User.query.filter_by(email=email).first():
            return "❌ E-mail já cadastrado."

        novo_user = User(nome=nome, email=email, senha_hash=senha_hash)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')



''' sistema de login/logout '''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha_hash = request.form['senha']

        # Busca o usuário no banco
        user = User.query.filter_by(email=email).first()

        # Verifica se encontrou e se a senha confere
        if user and user.check_password(senha_hash):
            # Loga o usuário usando Flask-Login e também guarda na sessão
            login_user(user)
            session['user_id'] = user.id
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('listar_carros'))
        else:
            flash('Email ou senha inválidos.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')




''' sistema de logout '''
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




''' sistema de exibir carros '''
@app.route('/cars')
def listar_carros():
    carros = Car.query.all()
    return render_template('cars.html', carros=carros)



''' sistema de adicionar carros (apenas para usuários logados) '''
@app.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        preco_dia_raw = request.form['preco_dia']
        # Validação básica: converter para float
        try:
            preco_dia = float(preco_dia_raw)
        except ValueError:
            flash('Preço inválido. Use um número, por exemplo: 120.00', 'error')
            return render_template('add_car.html')

        # Verifica se já existe um carro com mesma marca/modelo para este usuário
        existe = Car.query.filter_by(marca=marca, modelo=modelo, user_id=current_user.id).first()
        if existe:
            flash('Você já cadastrou esse carro anteriormente.', 'error')
            return render_template('add_car.html')

        novo_carro = Car(
            marca=marca,
            modelo=modelo,
            preco_dia=preco_dia,
            user_id=current_user.id
        )
        db.session.add(novo_carro)
        db.session.commit()
        flash('Carro adicionado com sucesso!', 'success')
        return redirect(url_for('listar_carros'))

    # Se não for POST, apenas renderiza o formulário
    return render_template('add_car.html')




''' sistema de dashboard '''
@app.route('/dashboard')
@login_required
def dashboard():
    carros = Car.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', carros=carros)





    




if __name__ == '__main__':
    app.run(debug=True)
