

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
    is_org = db.Column(db.Boolean)
    events_created = db.relationship('Event', backref='creator', lazy=True)


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    id_created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run(port=5000, debug=True)