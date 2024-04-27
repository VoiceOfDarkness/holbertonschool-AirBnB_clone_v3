#!/usr/bin/python3
"""
endpoint for places
"""
from flask import jsonify, request, abort

from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route("/cities/<city_id>/places", strict_slashes=False)
def places(city_id: str):
    """Return a places of the city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places = []
    for place in city.places:
        places.append(place.to_dict())

    return jsonify(places), 200


@app_views.route("/places/<place_id>", strict_slashes=False)
def place(place_id: str):
    """Return a place by id"""
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    return jsonify(place.to_dict()), 200


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_place(place_id: str):
    """Delete a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def add_place(city_id: str):
    """Add a City"""

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    data: dict = request.get_json()

    if data.get("user_id") is None:
        return jsonify({"error": "Missing user_id"}), 400

    user = storage.get(User, data["user_id"])
    if user is None:
        abort(404)

    if data.get("name") is None:
        return jsonify({"error": "Missing name"}), 400

    data["city_id"] = city_id

    place = Place(**data)

    place.save()

    return jsonify(place.to_dict()), 201


@app_views.route("/places/<place_id>", methods=["PUT"], strict_slashes=False)
def update_place(place_id: str):
    """Update a place"""

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    for key, value in data.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)

    place.save()

    return jsonify(place.to_dict()), 200


@app_views.route("/places_search", methods=["POST"], strict_slashes=False)
def place_search():

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    if not data or all(not val for val in data.values()):
        all_places = storage.all('Place').values()
        return jsonify([place.to_dict() for place in all_places]), 200

    places = []

    if data.get("states"):
        states = data["states"]
        places += [place for place in all_places
                   if place.city.state_id in states]

    if data.get("cities"):
        cities = data["cities"]
        places += [place for place in all_places if place.city_id in cities]

    if data.get("amenities"):
        amenities = data["amenities"]
        places = [place for place in places if all(amenity in place.amenities
                                                   for amenity in amenities)]

    return jsonify([place.to_dict() for place in places]), 200
