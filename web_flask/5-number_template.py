#!/usr/bin/python3
""" Flask framework """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return index page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB page """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ var text """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ var text """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>')
def check_int(n):
    """ return router val in int """
    return (f"{n} is a number")


@app.route('/number_template/<int:n>')
def number_template(n):
    """ return int """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
