from flask.ext.httpauth import HTTPBasicAuth
from schemas import ma, Sensordatas_schema
from flask import render_template, request, jsonify, abort, make_response
from sensors import app, db
from models import Sensordata, User
from flask_restful import Resource, Api, reqparse, reqparse
from datetime import datetime, timedelta
from faultDetection.faultDetector import correctfault

api = Api(app)
auth =HTTPBasicAuth()



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("main_page.html",
                               readings=db.session.query(Sensordata).order_by(Sensordata.time.desc()).limit(60).all())



@app.route("/visualisation")
def visualisation():


    # readings1 = db.session.query(Sensordata).filter(
    #     Sensordata.DeviceID == "PiJCCoffee",
    #     Sensordata.voc is not None,
    #     Sensordata.voc > 0,
    #     Sensordata.dht22 is not None,
    #     Sensordata.dht22 > 0,
    #     Sensordata.dht22 <= 100
    # ).order_by(Sensordata.time.asc()).limit(2880).all()
    #
    # JCCoffee, errors1 = Sensordatas_schema.dump(readings1)
    # JCCoffee = correctfault(JCCoffee)

    readings1 = db.session.query(Sensordata).filter(
        Sensordata.DeviceID == "PiJCCoffee"
    ).order_by(Sensordata.time.asc()).limit(2880).all()

    JCCoffee, errors1 = Sensordatas_schema.dump(readings1)
    JCCoffee = correctfault(JCCoffee)



    readings2 = db.session.query(Sensordata).filter(
        Sensordata.DeviceID == "PiJCLabRear",
        Sensordata.voc is not None,
        Sensordata.voc > 0,
        Sensordata.dht11 is not None,
        Sensordata.dht11 > 0,
        Sensordata.dht11 <= 100
    ).order_by(Sensordata.time.desc()).limit(2880).all()

    JCLab, errors2 = Sensordatas_schema.dump(readings2)

    readings3 = db.session.query(Sensordata).filter(
        Sensordata.DeviceID == "PiJHLabDoor",
        Sensordata.voc is not None,
        Sensordata.voc > 0,
        Sensordata.dht11 is not None,
        Sensordata.dht11 > 0,
        Sensordata.dht11 <= 100
    ).order_by(Sensordata.time.desc()).limit(2880).all()

    JHLab, errors3 = Sensordatas_schema.dump(readings3)

    print (JCLab)
    print (JHLab)

    return render_template('visualisation.html', JCCoffee=JCCoffee, JHLab=JHLab, JCLab=JCLab)



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
                   'pressure': reading.pressure,
                   'humidity': reading.humidity,
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
                   'pressure': reading.pressure,
                   'humidity': reading.humidity,
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
                   'pressure': data.pressure,
                   'humidity': data.humidity,
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

    sensordata = db.session.query(Sensordata).filter(Sensordata.time >= start, Sensordata.time <= end).order_by(Sensordata.time.asc()).all()
    data_array = []

    for data in sensordata:

        print(data.id)
        print(data.time)
        print("\n")


    for data in sensordata:
        reading = {'id': data.id,
                   'deviceid': data.DeviceID,
                   'datetime': data.time.strftime('%d-%m-%Y  %H:%M:%S'),
                   'pressure': data.pressure,
                   'humidity': data.humidity,
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
@app.route('/reading/<deviceid>', methods=['GET'])
def reading_latest(deviceid):
    data = db.session.query(Sensordata).filter(Sensordata.DeviceID == deviceid).order_by(Sensordata.time.desc()).first_or_404()

    reading = {'id': data.id,
               'deviceid': data.DeviceID,
               'datetime': data.time.strftime('%d-%m-%Y  %H:%M:%S'),
               'humidity': data.humidity,
               'pressure': data.pressure,
               'voc': data.voc,
               'dht11': data.dht11,
               'dht22': data.dht22,
               'uv': data.uv,
               'motion': data.motion
               }

    return jsonify(reading)


class AddSensorReading(Resource):

    # add reading and return what was committed to the database.
    # requests.post('http://localhost:8080/addreading', data={'temperature': '3', 'pressure': '5', 'light' : '6', 'device': 'PiA'}).json()
    @auth.login_required
    def post(self):

        if not 'device' in request.form:
            abort(400)

        reading = Sensordata(DeviceID=request.form.get("device"),
                             time=datetime.utcnow(),
                             humidity=request.form.get("humidity"),
                             pressure=request.form.get("pressure"),
                             voc=request.form.get("voc"),
                             co2=request.form.get("co2"),
                             dht11=request.form.get("dht11"),
                             dht22=request.form.get("dht22"),
                             uv=request.form.get("uv"),
                             motion=request.form.get("motion"),
                             light=request.form.get("light"))

        db.session.add(reading)
        db.session.commit()

        return {'id': reading.id,
                'deviceid' : reading.DeviceID,
                "datetime": reading.time.strftime('%d/%m/%Y  %H:%M:%S'),
                'humidity': reading.humidity,
                'pressure': reading.pressure,
                'voc': reading.voc,
                'co2': reading.co2,
                'dht11': reading.dht11,
                'dht22': reading.dht22,
                'uv': reading.uv,
                'motion': reading.motion,
                'light': reading.light
                }

api.add_resource(AddSensorReading, '/reading')


class AddUser(Resource):

    #add user using the API
    def post(self):

        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        return {'status': 'added'}


api.add_resource(AddUser, '/user')


# return json encoded 404 error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    return True


@app.route("/docs", methods=["GET", "POST"])
def docs():

    return render_template("api.html")


#route to return visualisation of two hours data for specified device as a visualisation
@app.route('/hourvisualisation/<deviceid>/<start>', methods=['GET'])
def hourvisualisation(deviceid, start):
    start = datetime.strptime(start, '%d-%m-%Y %H:%M:%S')
    end = start + timedelta(hours=5)

    readings = db.session.query(Sensordata).filter(
        Sensordata.time >= start,
        Sensordata.time <= end,
        Sensordata.DeviceID == deviceid
    ).order_by(Sensordata.time.asc()).limit(2880).all()


    data, errors1 = Sensordatas_schema.dump(readings)

    return render_template('hourvisualisation.html', data=data)
