#!/usr/bin/python3
"""
This module defines a Flask application that serves a
"Hello HBNB!" message.
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello():
    """
    Returns a "Hello HBNB!" message when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns a "HBNB" message when the /hbnb URL is accessed.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
