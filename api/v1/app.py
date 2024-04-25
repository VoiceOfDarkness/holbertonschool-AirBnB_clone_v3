#!/usr/bin/python3
import os

from api.v1.views import app_views
from flask import Flask
from models import storage

app = Flask(__name__)

HOST = os.getenv("HBNB_API_HOST", default="0.0.0.0")
PORT = os.getenv("HBNB_API_PORT", default=5000)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(HOST, PORT)
