#!/usr/bin/python3
""" A flask server to return id and name of a State object

Returns:
    _type_: _description_
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())

    print("states_list")
    print(states)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())
    # sort by name with case insensitive
    states = sorted(states, key=lambda state: state.name.lower())

    # store states in a dictionary where the key is state and
    # value is list of cities
    states_dict = {}
    for state in states:
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            states_dict[state] = sorted(
                state.cities, key=lambda city: city.name)
        else:
            states_dict[state] = sorted(
                state.cities(), key=lambda city: city.name.lower())

    # print(states_dict)
    # for state in states_dict:
    #     print(state.name)
    #     for city in states_dict[state]:
    #         print("         ",city.name)
    return render_template('8-cities_by_states.html',
                           states=states_dict)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states(id=None):

    if id:
        # get the State object with id = id
        state = storage.all(State).get('State.' + id)
        # if state is None, return 404
        if state is None:
            return render_template('9-states.html', found=0)
        # else, return the state
        else:
            # get all the cities in the state
            if os.getenv('HBNB_TYPE_STORAGE') == 'db':
                cities = sorted(
                    state.cities, key=lambda city: city.name.lower())

            else:
                cities = sorted(
                    state.cities(), key=lambda city: city.name.lower())

            return render_template('9-states.html',
                                   state=state, cities=cities, found=1)

    else:
        states = list(storage.all().values())
        states = sorted(states, key=lambda state: state.name.lower())
        return render_template('9-states.html', states=states, found=2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
