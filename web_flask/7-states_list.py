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


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    Renders an HTML page that displays a list of all State objects.
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
