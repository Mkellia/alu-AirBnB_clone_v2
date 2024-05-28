#!/usr/bin/python3
""" A script that starts a Flask web application and do some dummy stuff

Returns:
    _type_: _description_
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_is_cool(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    # start the flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
