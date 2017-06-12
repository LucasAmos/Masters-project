from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sensors import db, app
from sqlalchemy import DateTime
import datetime

migrate =Migrate(app, db)

class Sensordata(db.Model):

    __tablename__ = "Sensordata"

    dt = datetime.datetime.utcnow()

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(DateTime, default=dt)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    light = db.Column(db.Float)

