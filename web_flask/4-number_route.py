#!/usr/bin/python3
"""Intialize Flask Server"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello World"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hello hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """C is fun"""
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
