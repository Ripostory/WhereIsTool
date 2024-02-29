"""
Application entry point
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.classes.base import WIBase

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(model_class=WIBase)
db.init_app(app)

with app.app_context():
    db.create_all()

# Required to be down here so that routes aren't created before the app is created
# noinspection PyUnresolvedReferences
import src.error_handlers
# noinspection PyUnresolvedReferences
import src.api.location_api
