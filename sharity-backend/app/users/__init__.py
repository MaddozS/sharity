# User CRUD

from flask import Blueprint, request
from flask_restplus import Resource, Namespace, fields
from app.extensions import db
from app.orm_models.users_model import User
from app.schemas.users_schemas import UserSchema
from sqlalchemy.exc import SQLAlchemyError


users_blueprint = Blueprint('users', __name__, url_prefix='/api/users')
api_users = Namespace('Users', description="User's CRUD")


USERS = [
    {'id': '1', 'name': 'Felix'},
]

user_model = api_users.model('User', {
    'id': fields.Integer(readonly=True, description='The identifies of the user'),
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The email provided by the user'),
    'password': fields.String(required=True, description='The password provided by the user')
})


@api_users.route('/prueba')
class UsersCRUD(Resource):

    @api_users.doc('list_cats')
    @api_users.marshal_list_with(user_model)
    def get(self):
        users = User.query.all()
        users_schema = UserSchema(many=True)

        return users_schema.dump(users)

    @api_users.expect(user_model)
    @api_users.marshal_with(user_model, code=201)
    def post(self):
        payload = request.get_json()
        try:
            user = User(payload["username"], payload["email"], payload["password"])
            db.session.add(user)
            db.session.commit()
            return 'User added'

        except SQLAlchemyError as e:
            db.session.rollback()
            return f'error: {e}'
