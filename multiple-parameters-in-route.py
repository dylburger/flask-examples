""" Let's examine how to create an endpoint with multiple, variable parameters passed in the route
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ice-cream/<flavor>/<size>')
def return_ice_cream_info(flavor, size):
    """ Return the ice cream flavor and the size string passed by the user
    """
    return jsonify({'flavor': flavor, 'size': size})


if __name__ == "__main__":
    app.run(debug=True)
