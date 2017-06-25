from flask_migrate import Migrate
from sensors import db, app
from sqlalchemy import DateTime
import datetime

class Sensordata(db.Model):

    __tablename__ = "Sensordata"

    dt = datetime.datetime.utcnow()

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(DateTime, default=dt)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    light = db.Column(db.Float)
    voc = db.Column(db.Float)
    DeviceID = db.Column(db.TEXT)
    dht11 = db.Column(db.Float)
    dht22 = db.Column(db.Float)
    uv = db.Column(db.Float)
    motion = db.Column(db.Float)
