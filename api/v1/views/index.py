#!/usr/bin/python3
"""
This module contains the routes and views for the index of the API.
"""
from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200


@app_views.router('/stats', strict_slashes=False)
def stats():
    """Return stats of all classes in the storage."""
    data = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(data), 200
