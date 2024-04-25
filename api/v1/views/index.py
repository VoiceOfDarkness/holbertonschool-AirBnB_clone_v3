#!/usr/bin/python3

"""
This module contains the routes and views for the index of the API.
"""
from flask import jsonify

from api.v1.views import app_views
from models import amenity, city, place, review, state, storage, user


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200


@app_views.router('/stats', strict_slashes=False)
def stats():
    data = {
        "amenities": storage.count(amenity.Amenity),
        "cities": storage.count(city.City),
        "places": storage.count(place.Place),
        "reviews": storage.count(review.Review),
        "states": storage.count(state.State),
        "users": storage.count(user.User)
    }
    return jsonify(data), 200
