#!/usr/bin/python3
"""
endpoint for states
"""
import json

from flask import jsonify
from flask import request

from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False)
def states():
    """Return all states"""
    states = storage.all(State)
    return jsonify([state.to_dict() for state in states.values()]), 200


@app_views.route("/states/<state_id>", strict_slashes=False)
def state(state_id: str):
    """Return a state"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict()), 200


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id: str):
    """Delete a state"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"],
                 strict_slashes=False)
def add_state():
    """Add a state"""

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    if data.get("name") is None:
        return jsonify({"error": "Missing name"}), 400

    state = State(**data)

    state.save()

    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id: str):
    """Update a state"""

    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(State, key, value)

    storage.save()

    return jsonify(data), 200
