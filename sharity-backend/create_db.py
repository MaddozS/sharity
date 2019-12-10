

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://axel:Axelsharity@localhost/pruebas'
db = SQLAlchemy(app)


# Schemas those should be in the database, SQLALchemy
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
