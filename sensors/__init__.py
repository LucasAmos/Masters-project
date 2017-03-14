from flask import Flask, render_template
app = Flask(__name__)

from flask.ext.sqlalchemy import SQLAlchemy



if __name__ == "__main__":
    app.run()

import sensors.views
import sensors.database

db = SQLAlchemy(app)
