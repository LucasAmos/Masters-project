from flask_marshmallow import Marshmallow
from models import Sensordata
from marshmallow import Schema, fields

ma = Marshmallow()

class SensordataSchema(ma.Schema):

        close = fields.Str(attribute="voc")
        date = fields.DateTime(attribute="time")
        open = fields.Str(attribute="light")

        #fields = ('dht22', 'voc', 'light')


        model = Sensordata




Sensordata_schema = SensordataSchema()
Sensordatas_schema = SensordataSchema(many=True)

