from unittest import TestCase
from sensors.AQI import AQI


class TestCalculateMetric(TestCase):

    def test_humidity_bottom_bad_dropoff(self):
        metric = AQI.calculateMetric(0, 19.9, 0)
        self.assertEqual(metric[1], -1)

    def test_humidity_bottom_bad_boundary(self):
        metric = AQI.calculateMetric(0, 20, 0)
        self.assertEqual(metric[1], -1)

    def test_humidity_bottom_bad_lower(self):
        metric = AQI.calculateMetric(0, 20.1, 0)
        self.assertEqual(metric[1], -0.99)

    def test_humidity_bottom_bad_upper(self):
        metric = AQI.calculateMetric(0, 29.9, 0)
        self.assertEqual(metric[1], -0.01)

    def test_humidity_bottom_acceptable_boundary(self):
        metric = AQI.calculateMetric(0, 30, 0)
        self.assertEqual(metric[1], 0)


    def test_humidity_bottom_acceptable_lower(self):
        metric = AQI.calculateMetric(0, 30.1, 0)
        self.assertEqual(metric[1], 0.01)

    def test_humidity_bottom_acceptable_upper(self):
        metric = AQI.calculateMetric(0, 39.9, 0)
        self.assertEqual(metric[1], 0.99)

    def test_humidity_bottom_good_boundary(self):
        metric = AQI.calculateMetric(0, 40, 0)
        self.assertEqual(metric[1], 1)

    def test_humidity_bottom_good_lower(self):
        metric = AQI.calculateMetric(0, 40.1, 0)
        self.assertEqual(metric[1], 1)


    def test_humidity_good(self):
        metric = AQI.calculateMetric(0, 50, 0)
        self.assertEqual(metric[1], 1)

    def test_humidity_top_good_upper(self):
        metric = AQI.calculateMetric(0, 59.9, 0)
        self.assertEqual(metric[1], 1)

    def test_humidity_top_good_boundary(self):
        metric = AQI.calculateMetric(0, 60, 0)
        self.assertEqual(metric[1], 1)

    def test_humidity_top_acceptable_lower(self):
        metric = AQI.calculateMetric(0, 60.1, 0)
        self.assertEqual(metric[1], 0.99)

    def test_humidity_top_acceptable_upper(self):
        metric = AQI.calculateMetric(0, 69.9, 0)
        self.assertEqual(metric[1], 0.01)

    def test_humidity_top_bad_boundary(self):
        metric = AQI.calculateMetric(0, 70, 0)
        self.assertEqual(metric[1], 0)

    def test_humidity_top_bad_lower(self):
        metric = AQI.calculateMetric(0, 70.1, 0)
        self.assertEqual(metric[1], -0.01)

    def test_humidity_top_bad_upper(self):
        metric = AQI.calculateMetric(0, 79.9, 0)
        self.assertEqual(metric[1], -0.99)

    def test_humidity_top_bad_dropoff(self):
        metric = AQI.calculateMetric(0, 80, 0)
        self.assertEqual(metric[1], -1)
