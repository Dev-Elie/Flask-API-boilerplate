# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import config
from .db import db
from .routes import app as rootView

# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow

migrate = Migrate()
ma = Marshmallow()

def create_app(config_class=config.DevelopmentConfig):

    """Application-factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    app.register_blueprint(rootView)

    return app
