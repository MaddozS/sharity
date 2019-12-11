from flask_restplus import fields
from . import api_users

# This object is the representation of the user object in JSON, used by Swagger.
user_model = api_users.model('User', {
    'id': fields.Integer(readonly=True, description='The identifies of the user'),
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The email provided by the user'),
    'password': fields.String(required=True, description='The password provided by the user'),
    'is_org': fields.Boolean(description='Declares if the account is and organizational account or a user account')
})
