#!/usr/bin/python3
"""This module sets up a flask app and API"""
from models import storage
from api.v1.views import app_views
from sys import getenv


app = Flask(__name__)

app.register_blueprint(app_views)
app.url_sap.strict_slashes = True


@app.teardown_appcontext()
def app_teardown(exception):
    """removes the current storage session after each request"""
    storage.close()


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
