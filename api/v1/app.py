#!/usr/bin/python3
"""This module sets up a flask app and API"""
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from sys import getenv 


app = Flask(__name__)

app.register_blueprint(app_views)
app.url_sap.strict_slashes = True


@app.teardown_appcontext
def close_storage(exception):
        """Closes the storage on teardown."""
        storage.close()


if __name__ == "__main__":
        host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
        port = int(os.environ.get('HBNB_API_PORT', 5000))
        app.run(host=host, port=port, threaded=True)
