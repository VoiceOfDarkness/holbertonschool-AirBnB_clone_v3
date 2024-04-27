#!/usr/bin/python3
"""
endpoint for reviews of the places
"""
from flask import jsonify
from flask import request

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route("/places/<place_id>/reviews", strict_slashes=False)
def reviews(place_id: str):
    """Return a reviews of the place"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"}), 404

    reviews = []
    for review in place.reviews:
        reviews.append(place.to_dict())

    return jsonify(reviews), 200


@app_views.route("/reviews/<review_id>", strict_slashes=False)
def review(review_id: str):
    """Return a review by id"""
    review = storage.get(Review, review_id)

    if review is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(review.to_dict()), 200


@app_views.route("/reviews/<review_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_review(review_id: str):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews", methods=["POST"],
                 strict_slashes=False)
def add_review(place_id: str):
    """Add a Review"""

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"}), 404

    data: dict = request.get_json()

    if data.get("user_id") is None:
        return jsonify({"error": "Missing user_id"}), 400

    user = storage.get(User, data["user_id"])
    if user is None:
        return jsonify({"error": "Not found"}), 404

    if data.get("text") is None:
        return jsonify({"error": "Missing text"}), 400

    data["place_id"] = place_id

    review = Review(**data)

    review.save()

    return jsonify(place.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=["PUT"], strict_slashes=False)
def update_review(review_id: str):
    """Update a Review"""

    reviews = storage.get(Review, review_id)
    if reviews is None:
        return jsonify({"error": "Not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    for key, value in data.items():
        if key not in ["id", "user_id", "place_id",
                       "created_at", "updated_at"]:
            setattr(reviews, key, value)

    reviews.save()

    return jsonify(reviews.to_dict()), 200
