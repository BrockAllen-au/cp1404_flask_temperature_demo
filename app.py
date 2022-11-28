from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'Hello {name}'

@app.route('/f')
@app.route('/f/<celcius>')
def f(celcius=""):
    conversion = convert_celcius_to_fahrenheit(celsius=celcius)
    output = f"<h1>Converting: {celcius}c --> Fahrenheit</h1>\n{celcius}c = {conversion}f"
    return output


def convert_celcius_to_fahrenheit(celsius):
    """Convert celcius to fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
