#!/usr/bin/python3
""" Flask framework """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return page index """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return page hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return page router """
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
