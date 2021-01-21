#!/usr/bin/python3
"""Starts a Flask web application with seven routes"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
