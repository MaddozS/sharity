# User CRUD

from flask import Blueprint, request
from flask_restplus import Resource, Namespace
from app.extensions import db
from app.orm_models.models import User
from app.schemas.schemas import UserSchema
from sqlalchemy.exc import SQLAlchemyError

users_blueprint = Blueprint('users', __name__, url_prefix='/api/users')
api_users = Namespace('Users', description="User's CRUD")

from .swagger_utils import user_model


@api_users.route('/')
@api_users.response(500, "Couldn't add the user")
@api_users.response(201, "User added")
@api_users.response(200, "Action successfuly executed")
class UsersCRUD(Resource):

    @api_users.doc('list_users')
    @api_users.marshal_list_with(user_model)
    def get(self):
        """
        Get method for the user CRUD. Return all the users in the database
        """
        users = User.query.all()
        users_schema = UserSchema(many=True)

        return users_schema.dump(users), 200

    @api_users.doc('add_user')
    @api_users.expect(user_model)
    def post(self):
        """
        Post method for the user CRUD, insert a new user in the database (only one)
        """
        payload = request.get_json()

        try:
            user = User(username=payload["username"], 
                        email=payload["email"], 
                        password=payload["password"], 
                        is_org=payload["is_org"] if payload["password"] else False)

            db.session.add(user)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                    'error': e,
                    'message': "couldn't add the user",
                    'code': 500
                   }, 500

        return {
                'message': "User added",
                'code': 201
               }, 201

@api_users.route('/<int:id>')
@api_users.param('id', 'the identifier of the user')
@api_users.response(500, "Internal server error")
@api_users.response(204, "User updated/deleted")
@api_users.response(200, "Action successfuly executed")
class UserCRUDById(Resource):

    @api_users.doc('get_user')
    @api_users.marshal_with(user_model)
    def get(self, id):
        """
        Get method for the user CRUD. Return all the users in the database
        """
        try:
            user = User.query.filter_by(id=id).first()
            user_schema = UserSchema()

        except SQLAlchemyError as e:
            return {
                    'error': e,
                    'message': "Internal Server Error",
                    'code': 500
                   }, 500

        if user is None:
            return {
                    'message': "user not found",
                    'code': 400
                   }, 400
        else:
            return user_schema.dump(user), 200

    @api_users.expect(user_model)
    def put(self, id):
        """
        Put method for the user CRUD, update one user in the database
        """
        payload = request.get_json()

        try:
            user = User.query.filter_by(id=id).first()
            if user is not None:
                for key in payload:
                    if hasattr(user, key):
                        # Accessing to the attribute without declare its name directly
                        setattr(user, key, payload[key])
                db.session.commit()
            else:
                return {
                        'message': "user not found",
                        'code': 404
                       }, 404
        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                    'error': e._message(),
                    'message': "couldn't update the user",
                    'code': 500
                   }, 500

        return {
                'message': "User updated",
                'code': 200,
                'user': str(user)
               }, 200

    def delete(self, id):
        """
        Delete method for the user CRUD, delete a user in the database
        """

        try:
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                    'error': e._message(),
                    'message': "couldn't delete the user",
                    'code': 500
                   }, 500

        return {
                'message': "User deleted",
                'code': 200
               }, 200
