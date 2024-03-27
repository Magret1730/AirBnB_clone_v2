#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """function that displays HTML page"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("9-states.html", sorted_states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """function that displays HTML page associated with an ID"""
    states = storage.all(State)
    state = next((state for state in states.values() if state.id == id), None)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template("9-states.html", data=cities,
                               state_name=state.name)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the SQLAlchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
