from flask import Flask, render_template
app = Flask(__name__)

app.config["DEBUG"] = True


from flask.ext.sqlalchemy import SQLAlchemy



if __name__ == "__main__":
    app.run()


import sensors.database

db = SQLAlchemy(app)
import sensors.views
import sensors.models
