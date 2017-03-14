from flask import render_template

from sensors import app

@app.route("/")
def hello():
        return render_template("main_page.html")