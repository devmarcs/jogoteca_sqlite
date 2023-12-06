from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogoteca.sqlite3'
app.config['SECRET_KEY'] = 'marc123'



db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *
from usuario import *

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
    