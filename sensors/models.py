from sensors import db


class Sensordata(db.Model):

    __tablename__ = "Sensordata"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    light = db.Column(db.Float)

