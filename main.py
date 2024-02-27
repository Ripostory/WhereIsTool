from flask import Flask
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy

from src.classes.base import WIBase
from src.classes.item import Item
from src.classes.location import Location

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(model_class=WIBase)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api/v1/location")
def get_location():
    loc_session = db.session
    query = select(Location).where(Location.name.in_(["Kitchen", "Home"]))
    for location in loc_session.scalars(query):
        print(location)
    loc_session.close()
    return "Hello, World!"
