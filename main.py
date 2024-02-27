from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.classes.base import WIBase
from src.classes.item import Item
from src.classes.location import Location

app = Flask(__name__)

engine = create_engine("sqlite://", echo=True)
WIBase.metadata.create_all(engine)

with Session(engine) as session:
    home = Location(name="Home", sub_locations=[
        Location(name="Kitchen", items=[
            Item(name="USB"),
            Item(name="Cups"),
            Item(name="Plates")
        ])
    ], items=[
        Item(name="Unknown Item")
    ])

    session.add_all([home])
    session.commit()


@app.route("/api/v1/location")
def get_location():
    return "Hello, World!"
