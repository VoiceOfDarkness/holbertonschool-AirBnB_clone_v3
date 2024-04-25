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


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
