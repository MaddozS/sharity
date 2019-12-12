# User CRUD

from flask import Blueprint, request
from flask_restplus import Resource, Namespace
from app.extensions import db
from app.orm_models.models import Event, User
from app.schemas.schemas import EventSchema
from sqlalchemy.exc import SQLAlchemyError

events_blueprint = Blueprint('events', __name__, url_prefix='/api/events')
api_events = Namespace('Events', description="Event's CRUD")

from .swagger_utils import event_model_response, event_model_query


@api_events.route('/')
@api_events.response(500, "Couldn't add the user")
@api_events.response(201, "User added")
@api_events.response(200, "Action successfuly executed")
class UsersCRUD(Resource):

    @api_events.doc('list_events')
    @api_events.marshal_list_with(event_model_response)
    def get(self):
        """
        Get method for the user CRUD. Return all the users in the database
        """
        events = Event.query.all()
        events_schema = EventSchema(many=True)

        return events_schema.dump(events), 200

    @api_events.doc('add_event')
    @api_events.expect(event_model_query)
    def post(self):
        """
        Post method for the user CRUD, insert a new user in the database (only one)
        """
        payload = request.get_json()

        try:
            user_creator = User.query.filter_by(id=payload['user_id']).first()
            event = Event(name=payload["name"], description=payload["description"], creator=user_creator)

            db.session.add(event)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                    'error': e,
                    'message': "couldn't add the user",
                    'code': 500
                   }, 500

        return {
                'message': "Event created",
                'code': 201
               }, 201

'''
@api_events.route('/<int:id>')
@api_events.param('id', 'the identifier of the user')
@api_events.response(500, "Internal server error")
@api_events.response(204, "User updated/deleted")
@api_events.response(200, "Action successfuly executed")
class UserCRUDById(Resource):

    @api_events.doc('get_user')
    @api_events.marshal_with(user_model)
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

    @api_events.expect(user_model)
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
'''