from app import marshmallow
from app.orm_models.models import User, Event


class UserSchema(marshmallow.ModelSchema):
    class Meta:
        model = User

class EventSchema(marshmallow.ModelSchema):
    class Meta:
        include_fk = True
        model = Event

    creator = marshmallow.Nested(UserSchema, all=True)