from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask(__name__)
app.config["DEBUG"] = True
moment = Moment(app)


if __name__ == "__main__":
    app.run()

import sensors.database

db = SQLAlchemy(app)
import sensors.views
import sensors.models
