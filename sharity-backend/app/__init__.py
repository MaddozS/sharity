from instance.config import app_config


from flask import Flask
from flask_restplus import Api
from app.extensions import db, bcrypt, marshmallow, migrate

from app.users import api_users, users_blueprint
from app.random import api_random, rnd_blueprint


def create_app(config_name, api):

    app = Flask(__name__)
    app.config.from_object(app_config[str(config_name)])
    # app.config.from_pyfile('../instance/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Starting each flask extension
    db.init_app(app)
    bcrypt.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Registering all the blueprints
    app.register_blueprint(users_blueprint)
    app.register_blueprint(rnd_blueprint)

    with app.app_context():
        db.create_all()
        db.session.commit()

    return app


def create_api():
    api = Api(
        title='Sharity API',
        version='1.0',
        description="The API of Sharity's backend",
        doc="/api/documentation"
    )
    api.add_namespace(api_users, path='/api/users')
    api.add_namespace(api_random, path='/api/random')

    return api
