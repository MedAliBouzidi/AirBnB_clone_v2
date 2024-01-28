#!/usr/bin/python3
""" Starts a Flask web application that listens on 0.0.0.0, port 5000 """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """
        Displays an HTML page with a list of all State objects in DBStorage.
        States are sorted by name.
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db(exc):
    """ Remove the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
