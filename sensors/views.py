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


@app.route("/visualisation")
def visualisation():
    readings = Sensordata.query.all()
    data, errors = Sensordatas_schema.dump(readings)

    return render_template("visualisation.html", data3=data)


# return a reading given it's ID
@app.route('/readings/<reading_id>', methods=['GET'])
def get_reading(reading_id):

    reading = db.session.query(Sensordata).get(reading_id)

    datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

    print datetime_object

    return jsonify({'DateTime': reading.time.strftime('%d/%m/%Y  %H:%M:%S'),
                    'temperature': reading.temperature,
                    'pressure': reading.pressure, 'light': reading.light})


# return a json array of all readings
@app.route('/readings', methods=['GET'])
def get_readings():

    sensordata = Sensordata.query.order_by(Sensordata.id.desc())
    data_array = []

    for data in sensordata:

        reading = {'id': data.id,
                   "DateTime": data.time.strftime('%d/%m/%Y  %H:%M:%S'),
                   'temperature': data.temperature,
                   'pressure': data.pressure,
                   'light': data.light
                   }
        data_array.append(reading)

    return jsonify(data_array)


# return a json array of all readings between a two dates (inclusive at start, exclusive at end)
@app.route('/range/<start>/<end>', methods=['GET'])
def range(start, end):
    start = datetime.strptime(start, '%d %m %Y %H:%M:%S')
    end = datetime.strptime(end, '%d %m %Y %H:%M:%S')

    sensordata = db.session.query(Sensordata).filter(Sensordata.time >= start, Sensordata.time <= end).all()

    data_array = []

    for data in sensordata:
        reading = {'id': data.id,
                   "DateTime": data.time.strftime('%d/%m/%Y  %H:%M:%S'),
                   'temperature': data.temperature,
                   'pressure': data.pressure,
                   'light': data.light
                   }
        data_array.append(reading)

    return jsonify(data_array)



class AddSensorReading(Resource):

    def get(self):
        reading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        return {'DateTime': reading.time.strftime('%B %d %Y - %H:%M:%S'),
                'temperature': reading.temperature,
                'pressure': reading.pressure, 'light': reading.light}

    def post(self):
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
# requests.put('http://localhost:8080/addreading', data={'temperature': '3', 'pressure': '5', 'light' : '6'}).json()


class GetSensorReadings(Resource):

    def get(self):
        committedreading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        return {'time': committedreading.time.strftime('%B %d %Y - %H:%M:%S'),
                'temperature': committedreading.temperature,
                'pressure': committedreading.pressure, 'light': committedreading.light}


api.add_resource(GetSensorReadings, '/getreadings')
# example api usage
# requests.get('http://localhost:8080/getreading').json()