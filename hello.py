from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message":"Hello World!"})

@app.route("/login")
def login():
    return ("Welcome, you are logged!")
