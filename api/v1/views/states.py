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
def update_state():
    """Update a state"""

    if request.is_json:
        data: dict = request.get_json()
    else:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(State, key, value)

    storage.save()

    return jsonify(data), 201
