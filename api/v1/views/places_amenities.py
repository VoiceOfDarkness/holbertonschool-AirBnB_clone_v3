#!/usr/bin/python3
"""
endpoint for reviews of the places
"""
from flask import abort, jsonify

from api.v1.views import app_views
from models import DB_TYPE, storage
from models.amenity import Amenity
from models.place import Place


@app_views.route("/places/<place_id>/amenities", methods=["GET"])
def get_amenities(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if DB_TYPE == "db":
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        amenities = [storage.get(Amenity, id).to_dict()
                     for id in place.amenity_ids]
    return jsonify(amenities)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=["DELETE"])
def delete_amenity(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)
    if DB_TYPE == "db":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
    else:
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"])
def link_amenity(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)
    if DB_TYPE == "db":
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
    else:
        if amenity_id in place.amenity_ids:
            return jsonify(storage.get(Amenity, amenity_id).to_dict()), 200
        place.amenity_ids.append(amenity_id)
    storage.save()
    return jsonify(amenity.to_dict()), 201
