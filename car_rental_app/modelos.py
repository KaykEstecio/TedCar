from db import db
from flask_login import UserMixin


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    preco_dia = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='disponível')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Carro {self.marca} {self.modelo}>'
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    carros = db.relationship('Car', backref='proprietario', lazy=True)

    def __repr__(self):
        return f'<User {self.nome}>'
