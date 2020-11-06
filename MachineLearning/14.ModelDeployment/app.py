import os
from flask import Flask, request, session, jsonify, render_template

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

@app.route("/")
def get_answer():
    return render_template("index.html", predicted_class = "cat")
    # answer = 42
    # return f"The Answer: {answer}"

@app.route("/save_name/<string:name>")
def save_name(name):
    session["username"] = name
    return "Your username was saved! " + session["username"]

@app.route("/greet/")
def greet():
    name = session["username"]
    return f"Hi {name}!"


@app.route("/sum_custom/", methods = ["POST"])    
def sum_numbers_custom():
    a, b = 0, 0
    request_body = request.data.decode()
    parameters = request_body.split("\r\n")
    a = int(parameters[0].split("=")[1])
    b = int(parameters[1].split("=")[1])
    sum = a + b
    return f"{a} + {b} = {sum}"

@app.route("/sum/", methods = ["POST"])    
def sum_numbers_json():
    a = request.json["a"]
    b = request.json["b"]

    sum = a + b

    return jsonify({"a": a, "b": b, "sum": sum})

app.run()