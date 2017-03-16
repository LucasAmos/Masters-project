from flask import render_template, url_for, redirect, request

from sensors import app, db

from models import Comment




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"], temperature=request.form["temperature"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/wibbly")
def wibbly():
        return "my pointless route"