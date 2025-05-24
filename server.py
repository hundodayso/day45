from flask import Flask

app = Flask(__name__)




@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2V6am5oaDllNGVucnNzbDJpZG5jdTkzcXAzMmJzZXNraGthaGVpaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwYDIeZl/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)



#https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2V6am5oaDllNGVucnNzbDJpZG5jdTkzcXAzMmJzZXNraGthaGVpaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwYDIeZl/giphy.gif