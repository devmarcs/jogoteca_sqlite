from app import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __repr__(self):
        return '<Name %r>' % self.nome
    


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, username, nome, senha):
        self.username = username
        self.nome = nome
        self.senha = senha

    def __repr__(self):
        return '<Name %r>' % self.nome