#!/usr/bin/python3
""" Start a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display 'C' followed by text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Display 'Python' followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def number(num: int):
    """ Display 'n is a number'"""
    return '{} is a number'.format(num)


def StartFlask():
    """ Start a Flask web application """
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    StartFlask()
