from flask import Flask
import random


app = Flask(__name__)

number = random.randint(1, 9)
print(number)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2V6am5oaDllNGVucnNzbDJpZG5jdTkzcXAzMmJzZXNraGthaGVpaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwYDIeZl/giphy.gif'>")
@app.route("/<int:input>")
def user_input(input):
    if input == number:
        return (f"<h1 style=color:green>Your number is correct!"
                f"</h1> <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif input > number:
        return (f"<h1 style=color:red>{input} is too high!</h1> "
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif input < number:
        return (f"<h1 style=color:blue>{input} is too low!</h1> "
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)



