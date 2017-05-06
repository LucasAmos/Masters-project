from flask import render_template, request, jsonify, json
from sensors import app, db
from models import Sensordata
from flask_restful import Resource, Api
from datetime import datetime
api = Api(app)
from schemas import ma, Sensordatas_schema


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("main_page.html", readings=Sensordata.query.order_by(Sensordata.time.desc()).all())


@app.route("/iain", methods=["GET", "POST"])
def index():

        return render_template("iain.html")



@app.route("/visualisation")
def visualisation():
    readings = Sensordata.query.all()
    data, errors = Sensordatas_schema.dump(readings)

    return render_template("visualisation.html", data3 =data)





class AddSensorReading(Resource):

    def get(self):
        committedreading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        return {'time': committedreading.time.strftime('%B %d %Y - %H:%M:%S'),
                'temperature': committedreading.temperature,
                'pressure': committedreading.pressure, 'light': committedreading.light}

    def put(self):
        reading = Sensordata(time=datetime.utcnow(), temperature=request.form['temperature'],
                             pressure=request.form['pressure'], light=request.form['light'])
        db.session.add(reading)
        db.session.commit()

        committedreading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        return {'time': committedreading.time.strftime('%B %d %Y - %H:%M:%S'),
                'temperature': committedreading.temperature,
                'pressure': committedreading.pressure, 'light': committedreading.light}

api.add_resource(AddSensorReading, '/addreading')

# example api usage
# put('http://localhost:8080/addreading', data={'temperature': '3', 'pressure': '5', 'light' : '6'}).json()


class GetSensorReading(Resource):

    def get(self):
        committedreading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        return {'time': committedreading.time.strftime('%B %d %Y - %H:%M:%S'),
                'temperature': committedreading.temperature,
                'pressure': committedreading.pressure, 'light': committedreading.light}


api.add_resource(GetSensorReading, '/getreading')
