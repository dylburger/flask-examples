""" Let's examine how to set default values for the parameters tied to variable routes
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ice-cream/', defaults={'flavor': None})
@app.route('/ice-cream/<flavor>')
def return_ice_cream_info(flavor):
    """ Return the ice cream flavor the user enters as JSON
    """
    if flavor is None:
        return "Please provide a flavor of ice cream"

    return jsonify({'flavor': flavor})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
