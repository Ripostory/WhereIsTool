from flask import jsonify
from werkzeug.exceptions import NotFound

from app import app


@app.errorhandler(NotFound)
def handle_bad_request(e):
    return jsonify(message=e.name, status=e.code, mimetype='application/json'), e.code
