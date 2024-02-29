"""
Contains all the functions related to adding and modifying locations
"""
from flask import jsonify, request, abort
from src.classes.location import Location

from app import app, db


@app.route("/api/v1/location")
def get_location():
    """

    :return:
    """
    loc_session = db.session
    request_data = request.get_json()
    location = loc_session.get(Location, request_data['location_id'])
    if not location:
        abort(404)
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['POST'])
def add_location():
    """

    :return:
    """
    loc_session = db.session
    request_data = request.get_json()
    location = Location(name=request_data['name'], parent_location_id=request_data['parent_location_id'])
    loc_session.add(location)
    loc_session.commit()
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['PUT'])
def update_location():
    """

    :return:
    """
    loc_session = db.session
    request_data = request.get_json()
    location = loc_session.get(Location, request_data['location_id'])
    for key, value in request_data.items():
        location.update_from_key(key, value)
    loc_session.commit()
    return jsonify(message='OK', data=location.as_dict(), status=200, mimetype='application/json')


@app.route("/api/v1/location", methods=['DELETE'])
def delete_location():
    """

    :return:
    """
    request_data = request.get_json()
    location_id: int = request_data['location_id']
    loc_session = db.session
    target_loc = loc_session.get(Location, location_id)
    location_name = target_loc.name
    loc_session.delete(target_loc)
    loc_session.commit()
    return jsonify(message='OK', data=f'{location_name} deleted', status=200, mimetype='application/json')
