from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
@app.route("/bye")
@make_emphasis
def bye():
    return "Bye!"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)