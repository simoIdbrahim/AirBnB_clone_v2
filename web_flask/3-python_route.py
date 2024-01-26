#!/usr/bin/python3
""" Flask framework """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return index page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB page """
    return 'HBNB'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ return router page """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>')
def check_int(n):
    return (f"{n} is an integer")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
