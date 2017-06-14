from schemas import ma, Sensordatas_schema
from flask import render_template, request, jsonify, abort, make_response
from sensors import app, db
from models import Sensordata
from flask_restful import Resource, Api
from datetime import datetime
api = Api(app)


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
# requests.get('http://localhost:8080/readings/21').json()
@app.route('/readings/<reading_id>', methods=['GET'])
def get_reading_by_id(reading_id):

    reading = db.session.query(Sensordata).get(reading_id)

    if reading is None:
        abort(404)

    return jsonify({'DateTime': reading.time.strftime('%d/%m/%Y  %H:%M:%S'),
                    'temperature': reading.temperature,
                    'pressure': reading.pressure, 'light': reading.light})


# return a json array of all readings
# requests.get('http://localhost:8080/readings').json()
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
@app.route('/readings/<start>/<end>', methods=['GET'])
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


# return the most recent reading in the database
@app.route('/reading', methods=['GET'])
def reading_latest():
    data = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

    reading = {'id': data.id,
               'deviceid' : data.DeviceID,
               "DateTime": data.time.strftime('%d/%m/%Y  %H:%M:%S'),
               'temperature': data.temperature,
               'pressure': data.pressure,
               'light': data.light
               }

    return jsonify(reading)


@app.route('/add', methods=['POST'])
def add_reading():

    print request.json()

    reading = {'a': 'b'}
    return jsonify(reading)


# add reading and return what was commmitted to the database.
# requests.post('http://localhost:8080/addreading', data={'temperature': '3', 'pressure': '5', 'light' : '6', 'device': 'PiA'}).json()

class AddSensorReading(Resource):

    def post(self):

        if not 'device' in request.form:
           abort(400)

        reading = Sensordata(time=datetime.utcnow(), temperature=request.form['temperature'],
                             pressure=request.form['pressure'], light=request.form['light'],
                             DeviceID=request.form['device'])
        db.session.add(reading)
        db.session.commit()

        return {'id': reading.id,
                'deviceid' : reading.DeviceID,
                "DateTime": reading.time.strftime('%d/%m/%Y  %H:%M:%S'),
                'temperature': reading.temperature,
                'pressure': reading.pressure,
                'light': reading.light
                }

api.add_resource(AddSensorReading, '/addreading')


# return json encoded 404 error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
