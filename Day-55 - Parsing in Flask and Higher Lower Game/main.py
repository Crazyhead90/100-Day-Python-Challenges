from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</br>"
    return wrapper_function


def make_emphasize(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route('/')
def hello_word():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src=https://media.giphy.com/media/12ELmx0C4EFKcE/giphy.gif width=200>'


@app.route("/bye")
@make_bold
@make_emphasize
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
