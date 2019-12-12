from flask_restplus import fields
from . import api_events

# This object is the representation of the user object in JSON, used by Swagger.

event_model_response = api_events.model('Event Response', {
    'id': fields.Integer(readonly=True, description='The identifier of the event'),
    'name': fields.String(readonly=True, description='The name of the event'),
    'description': fields.String(readonly=True, description='The description of the event'),
    'creator_id': fields.Integer(readonly=True, description='The user who created the event', attribute='creator.id'),
    'creator_username': fields.String(readonly=True, description='The user who created the event', attribute='creator.username')
})

event_model_query = api_events.model('Event Query', {
    'id': fields.Integer(readonly=True, description='The identifier of the event'),
    'name': fields.String(required=True, description='The name of the event'),
    'description': fields.String(required=True, description='The description of the event'),
    'user_id': fields.Integer(required=True, description='The user who created the event')
})