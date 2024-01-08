#!/usr/bin/python3
"""Create a route /status on the object app_views"""
from api.v1.views.index import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=('GET'))
def api_status():
    """ returns a json response for restful api status"""
    response = ({'status': 'OK'})
    return jsonify(response)
