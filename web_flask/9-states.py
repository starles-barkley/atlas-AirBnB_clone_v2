#!/usr/bin/python3
'''This module starts a Flask web app'''

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
