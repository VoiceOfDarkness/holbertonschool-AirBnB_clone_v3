#!/usr/bin/python3
"""
This module defines a Flask application that serves a
"Hello HBNB!" message.
"""

from flask import Flask
from flask.templating import render_template

from models import storage


app = Flask("__name__", template_folder="web_flask/templates",
            static_folder="web_flask/static")
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.teardown_appcontext
def teardown(exception):
    """
    Closes the current SQLAlchemy session.
    """
    try:
        storage.close()
    except exception as e:
        print(e)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays an HTML page with the states and cities listed in the storage.
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
