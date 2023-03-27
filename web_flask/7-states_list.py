#!/usr/bin/python3
""" Start a Flask web application """

from flask import Flask
from flask import render_template
from models import storage

def StartFlask():
    """ Start a Flask web application """
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """ Display List of States """
        states = storage.all('State')
        print(states)
        return render_template('7-states_list.html', states=states.values())
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    StartFlask()
