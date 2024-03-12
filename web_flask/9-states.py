#!/usr/bin/python3
''' This module starts an application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states_by_id.html', state=state, cities=cities)
    else:
        return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
