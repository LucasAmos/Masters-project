from flask import render_template

from sensors import app, db

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route("/")
def hello():
        return render_template("main_page.html")