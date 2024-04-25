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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Returns a message containing the value of the text variable.
    """
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def text(text):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
