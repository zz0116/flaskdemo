from flask import render_template, jsonify

from app import app


@app.route("/")
def index():
    return render_template("index.html", content="See here ")


@app.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg="hello world!")
