from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sjoerd")
def hello():
    return "Hello, Sjoerd!"
