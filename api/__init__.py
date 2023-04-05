from flasgger import Swagger
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# App config
app = Flask(__name__)
app.config.from_object("config")

# Database config
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# API config
api = Api(app)

Swagger(app)

from .models import todo_model
from .views import todo_views
