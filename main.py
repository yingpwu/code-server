from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    message = "<h1> Code-Server-API 首页<h1>"
    return message