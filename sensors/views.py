from flask import render_template, url_for, redirect, request

from sensors import app, db

from models import Sensordata




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", readings=Sensordata.query.all())

    reading = Sensordata(temperature=request.form["temperature"], light=request.form["light"], pressure=request.form["pressure"])
    db.session.add(reading)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/wibbly")
def wibbly():
        return "my pointless route"