#!/usr/bin/python3
"""
This module contains the Flask application for the AirBnB clone API.

It creates a Flask app, registers the blueprint for the API views, and sets up
the host and port for the app to run.

Functions:
    close_session: A decorator function to close the database session after
    each request.

Variables:
    HOST: The host IP address for the app to run on.
    PORT: The port number for the app to run on.
"""

import os

from flask import Flask
from flask import jsonify
from flask_cors import CORS  # type: ignore

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})

HOST = os.getenv("HBNB_API_HOST", default="0.0.0.0")
PORT = os.getenv("HBNB_API_PORT", default=5000)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    """
    Closes the database session after each request.

    Args:
        exception: The exception raised during the request, if any.
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors (i.e. page not found).
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(HOST, PORT)
