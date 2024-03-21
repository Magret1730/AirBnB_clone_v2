#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """function that displays hello HBNB on the web page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """function that displays HBNB on the web page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """function that display C followed by the value of the text variable
    replace underscore _ symbols with a space"""
    text_space = text.replace('_', ' ')
    return "C {}".format(text_space)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """function that display Python followed by the value of the text variable
    replace underscore _ symbols with a space"""
    text_space = text.replace('_', ' ')
    return "Python {}".format(text_space)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """function that displays hello HBNB on the web page"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """function that displays hello HBNB on the web page"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
