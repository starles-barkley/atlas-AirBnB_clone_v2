#!/usr/bin/python3
'''This module starts a Flask web app'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n: int):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    oddness = ""
    if n % 2 == 0:
        oddness = "even"
    else:
        oddness = "odd"
    return render_template("6-number_odd_or_even.html", n=n, oddness=oddness)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states_dict = storage.all(State)
    states = {state_id: state for state_id, state in states_dict.items()}
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    for state in sorted_states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.route('/states', strict_slashes=False)
def state():
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
