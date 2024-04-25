#!/usr/bin/python3

"""
This module contains the routes and views for the index of the API.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200
