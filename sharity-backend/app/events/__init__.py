# User CRUD

from flask import Blueprint, request, abort
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
            abort(500, "Could't add the event", trace=e._message())

        return {
            'message': "Event created",
            'code': 201
        }, 201


@api_events.route('/<int:id>')
@api_events.param('id', 'the identifier of the user')
@api_events.response(500, "Internal server error")
@api_events.response(204, "User updated/deleted")
@api_events.response(404, "Not found")
class UserCRUDById(Resource):

    @api_events.doc('get_event')
    @api_events.marshal_with(event_model_response, description="User found", code=200)
    def get(self, id):
        """
        Get method for the user CRUD. Return all the users in the database
        """
        try:
            event = Event.query.filter_by(id=id).first()
            event_schema = EventSchema()

        except SQLAlchemyError as e:
            abort(500, "Internal Server Error", trace=e._message())

        if event is None:
            abort(404, 'Event not found')

        else:
            return event_schema.dump(event), 200

    @api_events.expect(event_model_query)
    def put(self, id):
        """
        Put method for the user CRUD, update one user in the database
        """
        payload = request.get_json()

        try:
            event = Event.query.filter_by(id=id).first()

            if event is not None:
                for key in payload:
                    if hasattr(event, key) and key != "user_id":
                        # Accessing to the attribute without declare its name directly
                        setattr(event, key, payload[key])

                db.session.commit()
            else:
                abort(404, 'Event not found')

        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, "Couldn't update the event", trace=e._message())

        return {
            'message': "Event updated",
            'code': 200
        }, 200

    def delete(self, id):
        """
        Delete method for the user CRUD, delete a user in the database
        """

        try:
            event = Event.query.filter_by(id=id).first()
            db.session.delete(event)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, "Couldn't delete the event", trace=e._message())

        return {
            'message': "Event deleted",
            'code': 200
        }, 200
