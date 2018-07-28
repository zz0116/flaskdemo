from flask import request, render_template

from app import app


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        return render_template("home.html", username=name, password=pwd)
    return render_template("login.html")
