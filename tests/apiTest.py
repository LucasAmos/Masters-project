from sensors import db, views, app
from sensors.models import Sensordata
from datetime import datetime

import unittest

class apiTestCase(unittest.TestCase):

    def setUp(self):

        app.post('/addreading', data=dict(
        temperature=22.2,
        pressure=33.3,
            light=44.4
    ), follow_redirects=True)


    def testApi(self):
        committedreading = db.session.query(Sensordata).order_by(Sensordata.id.desc()).first()

        print committedreading.light

        self.assertEquals(committedreading.temperature, 22.2)
