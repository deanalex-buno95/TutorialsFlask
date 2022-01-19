"""
Practical 10:
Question 3
app.py
"""


from flask import Flask

app = Flask(__name__)

PORT_NUMBER = 8500


@app.route('/')
def hello_world():
    """ Standard Page """
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """ Greeting Page """
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<temperature_in_celcius>')
def f(temperature_in_celcius=0):
    """ Temperature Page """
    try:
        return str((float(temperature_in_celcius) * (9/5)) + 32)
    except ValueError:
        return "This value cannot be converted!"


if __name__ == '__main__':
    app.run(debug=True, port=PORT_NUMBER)
