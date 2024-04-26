#!/usr/bin/python3
"""
endpoint for users
"""
from flask import jsonify
from flask import request

from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route("/users", strict_slashes=False)
def users():
    """Return all users"""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()]), 200


@app_views.route("/users/<user_id>", strict_slashes=False)
def user(user_id: str):
    """Return a user"""
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user.to_dict()), 200


@app_views.route("/users/<user_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_user(user_id: str):
    """Delete a user"""
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route("/users", methods=["POST"],
                 strict_slashes=False)
def add_user():
    """Add a user"""

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    if data.get("email") is None:
        return jsonify({"error": "Missing email"}), 400

    if data.get("password") is None:
        return jsonify({"error": "Missing password"}), 400

    user = User(**data)

    user.save()

    return jsonify(user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id: str):
    """Update a user"""

    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(user, key, value)

    user.save()

    return jsonify(user.to_dict()), 200
