import sys
from importlib import util
from pathlib import Path

APP_PATH = Path(__file__).resolve().parents[1] / 'app.py'

spec = util.spec_from_file_location('app', str(APP_PATH))
mod = util.module_from_spec(spec)
app_dir = str(APP_PATH.parent)
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)
spec.loader.exec_module(mod)

app = mod.app
from modelos import User, Car
from db import db
from werkzeug.security import generate_password_hash


with app.app_context():
    # cria um usuário de teste, se não existir
    if not User.query.filter_by(email='teste@example.com').first():
        u = User(nome='Teste', email='teste@example.com', senha_hash=generate_password_hash('1234'))
        db.session.add(u)
        db.session.commit()

with app.test_client() as c:
    # login
    resp = c.post('/login', data={'email': 'teste@example.com', 'senha': '1234'}, follow_redirects=True)
    print('LOGIN STATUS', resp.status_code)
    # adiciona carro
    resp2 = c.post('/add_car', data={'marca': 'Fiat', 'modelo': 'Uno', 'preco_dia': '120.00'}, follow_redirects=True)
    print('ADD STATUS', resp2.status_code)
    # lista carros
    resp3 = c.get('/cars')
    print('CARS PAGE STATUS', resp3.status_code)
    print(resp3.data.decode())
