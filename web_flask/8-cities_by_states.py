#!/usr/bin/python3
"""
This module defines a Flask application that serves a
"Hello HBNB!" message.
"""

from flask import Flask
from flask.templating import render_template
from models import storage

app = Flask("__name__", template_folder="web_flask/templates")


@app.teardown_appcontext
def teardown(exception):
    """
    Closes the current SQLAlchemy session.
    """
    try:
        storage.close()
    except exception as e:
        print(e)


@app.route("/cities_by_states", strict_slashes=False)
def city_by_state():
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
