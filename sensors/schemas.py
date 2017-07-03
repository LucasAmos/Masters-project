from flask_marshmallow import Marshmallow
from models import Sensordata

ma = Marshmallow()


class SensordataSchema(ma.Schema):
    class Meta:
        # fields = ('time','temperature', 'pressure', 'light')
        fields = ('time', 'dht22', 'voc', 'light')

        model = Sensordata


Sensordata_schema = SensordataSchema()
Sensordatas_schema = SensordataSchema(many=True)

