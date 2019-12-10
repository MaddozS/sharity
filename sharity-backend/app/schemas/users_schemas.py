from app import marshmallow
from app.orm_models.users_model import User


class UserSchema(marshmallow.ModelSchema):
    class Meta:
        model = User
