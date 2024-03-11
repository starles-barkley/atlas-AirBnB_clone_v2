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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
