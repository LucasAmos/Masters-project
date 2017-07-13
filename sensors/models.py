from passlib.apps import custom_app_context as pwd_context
from sensors import db, app
from sqlalchemy import DateTime
import datetime

class Sensordata(db.Model):

    __tablename__ = "Sensordata"

    dt = datetime.datetime.utcnow()

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(DateTime, default=dt)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    voc = db.Column(db.Float)
    DeviceID = db.Column(db.TEXT)
    dht11 = db.Column(db.Float)
    dht22 = db.Column(db.Float)
    uv = db.Column(db.Float)
    motion = db.Column(db.Float)
    light = db.Column(db.Float)
    co2 = db.Column(db.Float)



class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
