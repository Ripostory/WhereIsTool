from flask import Flask, jsonify, request, abort
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

import src.error_handlers


@app.route("/api/v1/location")
def get_location():
    loc_session = db.session
    request_data = request.get_json()
    location = loc_session.get(Location, request_data['location_id'])
    if not location:
        abort(404)
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['POST'])
def add_location():
    loc_session = db.session
    request_data = request.get_json()
    location = Location(name=request_data['name'], parent_location_id=request_data['parent_location_id'])
    loc_session.add(location)
    loc_session.commit()
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['PUT'])
def update_location():
    loc_session = db.session
    request_data = request.get_json()
    location = loc_session.get(Location, request_data['location_id'])
    for key, value in request_data.items():
        location.update_from_key(key, value)
    loc_session.commit()
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['DELETE'])
def delete_location():
    request_data = request.get_json()
    location_id: int = request_data['location_id']
    loc_session = db.session
    target_loc = loc_session.get(Location, location_id)
    location_name = target_loc.name
    loc_session.delete(target_loc)
    loc_session.commit()
    return jsonify(message='OK', data=f'{location_name} deleted', status=200, mimetype='application/json')
