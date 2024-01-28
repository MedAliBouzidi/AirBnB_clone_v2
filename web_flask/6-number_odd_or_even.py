#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_bnb():
    """ return "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb')
def bnb():
    """ return "HBNB" """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """ return a text from path variable """
    return f'C {text.replace("_", " ")}'


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """ return a text from path variable with default value """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>')
def number(n):
    """ number route """
    return f'{n:d} is a number'


@app.route('number/template/<int:n>')
def number_template(n):
    """ number template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Show if the number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
