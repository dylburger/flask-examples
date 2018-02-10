""" Let's examine how to set default values for the parameters tied to variable routes
"""
from flask import Flask, jsonify

app = Flask(__name__)


# You can define multiple rules tied to the same function
@app.route('/ice-cream/', defaults={'flavor': 'chocolate'})
@app.route('/ice-cream/<flavor>')
def return_ice_cream_info(flavor):
    """ Return the ice cream flavor the user enters as JSON
    """
    return jsonify({'flavor': flavor})


if __name__ == "__main__":
    app.run(debug=True)
