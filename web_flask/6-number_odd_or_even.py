#!/usr/bin/python3
""" Start a Flask web application """

from flask import Flask
from flask import render_template


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


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num: int):
    """ Display template if number """
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def number_odd_or_even(num: int):
    """ Display template if number """
    res = 'even' if num % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', num=num, odd=res)


def StartFlask():
    """ Start a Flask web application """
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    StartFlask()
