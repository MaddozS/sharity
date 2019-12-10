from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate(compare_type=True)
db = SQLAlchemy()
bcrypt = Bcrypt()
marshmallow = Marshmallow()
