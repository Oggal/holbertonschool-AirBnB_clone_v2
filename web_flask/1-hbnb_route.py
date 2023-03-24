#!/usr/bin/python3
""" Start a Flask web application """

import flask


def StartFlask():
    """ Start a Flask web application """
    app = flask.Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello():
        """ Display 'Hello HBNB!' """
        return 'Hello HBNB!'
    
    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """ Display 'HBNB' """
        return 'HBNB'

    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    StartFlask()