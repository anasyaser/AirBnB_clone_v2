#!/usr/bin/python3
"""Intialize Flask Server"""
from flask import Flask
from flask import render_template


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
    """Python is cool"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Print integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render Integer"""
    if (n % 2):
        return render_template('6-number_odd_or_even.html',
                               number=n, status='odd')
    return render_template('6-number_odd_or_even.html', number=n, status='even')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
