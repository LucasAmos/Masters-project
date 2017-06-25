from schemas import ma, Sensordatas_schema
from flask import render_template, request, jsonify, abort, make_response
from sensors import app, db
from models import Sensordata
from flask_restful import Resource, Api, reqparse, reqparse
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


# return a json array of all readings
# requests.get('http://localhost:8080/readings').json()
@app.route('/readings', methods=['GET'])
def readings():

    sensordata = Sensordata.query.order_by(Sensordata.id.desc())
    data_array = []

    for reading in sensordata:

        reading = {'id': reading.id,
                   'deviceid': reading.DeviceID,
                   'datetime': reading.time.strftime('%d-%m-%Y  %H:%M:%S'),
                   'temperature': reading.temperature,
                   'pressure': reading.pressure,
                   'light': reading.light,
                   'voc': reading.voc,
                   'dht11': reading.dht11,
                   'dht22': reading.dht22,
                   'uv': reading.uv,
                   'motion': reading.motion
                   }
        data_array.append(reading)

    return jsonify(data_array)


# return a json array of all readings for a specific deviceid
# requests.get('http://localhost:8080/readings').json()
@app.route('/readings/<deviceid>', methods=['GET'])
def deviceidreadings(deviceid):

    sensordata = db.session.query(Sensordata).filter(Sensordata.DeviceID == deviceid).all()

    data_array = []

    for reading in sensordata:

        reading = {'id': reading.id,
                   'deviceid': reading.DeviceID,
                   'datetime': reading.time.strftime('%d-%m-%Y  %H:%M:%S'),
                   'temperature': reading.temperature,
                   'pressure': reading.pressure,
                   'light': reading.light,
                   'voc': reading.voc,
                   'dht11': reading.dht11,
                   'dht22': reading.dht22,
                   'uv': reading.uv,
                   'motion': reading.motion
                   }
        data_array.append(reading)

    return jsonify(data_array)

# return a json array of all readings between two dates (inclusive at start, exclusive at end) and for a specific
# deviceid
# requests.get('http://localhost:8080/readings/19-03-2017 00:00:00/14-06-2017 00:00:00').json()
@app.route('/readings/<start>/<end>/<deviceid>', methods=['GET'])
def deviceidrange(start, end, deviceid):
    start = datetime.strptime(start, '%d-%m-%Y %H:%M:%S')
    end = datetime.strptime(end, '%d-%m-%Y %H:%M:%S')

    sensordata = db.session.query(Sensordata).filter(Sensordata.time >= start, Sensordata.time <= end, Sensordata.DeviceID == deviceid).all()
    data_array = []

    for data in sensordata:
        reading = {'id': data.id,
                   'deviceid': data.DeviceID,
                   'datetime': data.time.strftime('%d-%m-%Y  %H:%M:%S'),
                   'temperature': data.temperature,
                   'pressure': data.pressure,
                   'light': data.light,
                   'voc': data.voc,
                   'dht11': data.dht11,
                   'dht22': data.dht22,
                   'uv': data.uv,
                   'motion': data.motion
                   }
        data_array.append(reading)

    return jsonify(data_array)



# return a json array of all readings between two dates (inclusive at start, exclusive at end)
# requests.get('http://localhost:8080/readings/19-03-2017 00:00:00/14-06-2017 00:00:00').json()
@app.route('/readings/<start>/<end>', methods=['GET'])
def range(start, end):
    start = datetime.strptime(start, '%d-%m-%Y %H:%M:%S')
    end = datetime.strptime(end, '%d-%m-%Y %H:%M:%S')

    sensordata = db.session.query(Sensordata).filter(Sensordata.time >= start, Sensordata.time <= end).all()
    data_array = []

    for data in sensordata:
        reading = {'id': data.id,
                   'deviceid': data.DeviceID,
                   'datetime': data.time.strftime('%d-%m-%Y  %H:%M:%S'),
                   'temperature': data.temperature,
                   'pressure': data.pressure,
                   'light': data.light,
                   'voc': data.voc,
                   'dht11': data.dht11,
                   'dht22': data.dht22,
                   'uv': data.uv,
                   'motion': data.motion
                   }
        data_array.append(reading)

    return jsonify(data_array)


# return the most recent reading in the database
# requests.get('http://localhost:8080/reading').json()
@app.route('/reading', methods=['GET'])
def reading_latest():
    data = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

    reading = {'id': data.id,
               'deviceid' : data.DeviceID,
               "time": data.time.strftime('%d-%m-%Y  %H:%M:%S'),
               'temperature': data.temperature or None,
               'pressure': data.pressure or None,
               'light': data.light or None,
               'voc': data.voc or None
               }

    return jsonify(reading)


# return a reading given it's ID
# requests.get('http://localhost:8080/readings/21').json()
@app.route('/reading/<reading_id>', methods=['GET'])
def get_reading_by_id(reading_id):

    reading = db.session.query(Sensordata).get(reading_id)

    if reading is None:
        abort(404)

    return jsonify({'id': reading.id,
                    'deviceid': reading.DeviceID,
                    'datetime': reading.time.strftime('%d-%m-%Y  %H:%M:%S'),
                    'temperature': reading.temperature,
                    'pressure': reading.pressure,
                    'light': reading.light,
                    'voc': reading.voc,
                    'dht11': reading.dht11,
                    'dht22': reading.dht22,
                    'uv': reading.uv,
                    'motion': reading.motion
                    })

# add reading and return what was commmitted to the database.
# requests.post('http://localhost:8080/addreading', data={'temperature': '3', 'pressure': '5', 'light' : '6', 'device': 'PiA'}).json()


class AddSensorReading(Resource):

    def post(self):

        if not 'device' in request.form:
            abort(400)

        reading = Sensordata(DeviceID=request.form.get("device"),
                             time=datetime.utcnow(),
                             temperature=request.form.get("temperature"),
                             pressure=request.form.get("pressure"),
                             light=request.form.get("light"),
                             voc=request.form.get("voc"),
                             dht11=request.form.get("dht11"),
                             dht22=request.form.get("dht22"),
                             uv=request.form.get("uv"),
                             motion=request.form.get("motion"))

        db.session.add(reading)
        db.session.commit()

        return {'id': reading.id,
                'deviceid' : reading.DeviceID,
                "datetime": reading.time.strftime('%d/%m/%Y  %H:%M:%S'),
                'temperature': reading.temperature,
                'pressure': reading.pressure,
                'light': reading.light,
                'voc': reading.voc,
                'dht11': reading.dht11,
                'dht22': reading.dht22,
                'uv': reading.uv,
                'motion': reading.motion
                }

api.add_resource(AddSensorReading, '/reading')


# return json encoded 404 error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
