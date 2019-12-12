from app.extensions import db


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
