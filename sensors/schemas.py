from flask_marshmallow import Marshmallow
from models import Sensordata
from marshmallow import Schema, fields

ma = Marshmallow()

class SensordataSchema(ma.Schema):

        voc = fields.Str(attribute="voc")
        date = fields.DateTime(attribute="time")
        dht22 = fields.Str(attribute="dht22")

        #fields = ('dht22', 'voc', 'light')


        model = Sensordata




Sensordata_schema = SensordataSchema()
Sensordatas_schema = SensordataSchema(many=True)

