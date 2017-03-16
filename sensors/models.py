from sensors import db

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    light = db.Column(db.Float)

