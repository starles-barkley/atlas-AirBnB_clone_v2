#!/usr/bin/python3
'''This starts an application'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a list of states and their associated cities
    """
    states_dict = storage.all(State)
    states = {state_id: state for state_id, state in states_dict.items()}
    # Sort states by name
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    # Sort cities within each state by name
    for state in sorted_states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
