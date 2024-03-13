#!/usr/bin/python3
'''This module starts a Flask web app'''

import sys
from flask import Flask
from flask import render_template
from flask import g
import logging
from models import storage, env
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_route(id=0):
    res = 0
    title = "HBNB"
    if id == 0:
        res = storage.all("State").values()
    else:
        for state in storage.all("State"):
            if state.split(".")[1] == id:
                res = storage.all("State")[state]
    if id != 0 and res == 0:
        title = "Not found"
        id = 'Not found'

    return render_template("9-states.html", res=res, id=id, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    from models import storage
    from models.state import State
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    from models import storage
    from models.state import State

    states = storage.all(State).values()
    #  generator expression to find valid cases of state.id == id
    state = next((state for state in states if state.id == id), None)

    if state:
        return render_template('9-states.html', state=state, not_found=False)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close current SQLAlchemy session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
