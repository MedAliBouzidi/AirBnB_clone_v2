#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

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
    return f'python {text}'


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
