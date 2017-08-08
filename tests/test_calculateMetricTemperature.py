from unittest import TestCase
from sensors.AQI import AQI


class TestCalculateMetric(TestCase):

    def test_temperature_bottom_bad_dropoff(self):
        metric = AQI.calculateMetric(19.9, 0, 0)
        self.assertEqual(metric[0], -1)

    def test_temperature_bottom_bad_boundary(self):
        metric = AQI.calculateMetric(20, 0, 0)
        self.assertEqual(metric[0], -1)

    def test_temperature_bottom_bad_lower(self):
        metric = AQI.calculateMetric(20.1, 0, 0)
        self.assertEqual(metric[0], -0.9)

    def test_temperature_bottom_bad_upper(self):
        metric = AQI.calculateMetric(20.9, 0, 0)
        self.assertEqual(metric[0], -0.1)

    def test_temperature_bottom_acceptable_boundary(self):
        metric = AQI.calculateMetric(21, 0, 0)
        self.assertEqual(metric[0], 0)


    def test_temperature_bottom_acceptable_lower(self):
        metric = AQI.calculateMetric(21.1, 0, 0)
        self.assertEqual(metric[0], 0.05)

    def test_temperature_bottom_acceptable_upper(self):
        metric = AQI.calculateMetric(22.9, 0, 0)
        self.assertEqual(metric[0], 0.95)

    def test_temperature_bottom_good_boundary(self):
        metric = AQI.calculateMetric(23, 0, 0)
        self.assertEqual(metric[0], 1)

    def test_temperature_bottom_good_lower(self):
        metric = AQI.calculateMetric(23.1, 0, 0)
        self.assertEqual(metric[0], 1)


    def test_temperature_good(self):
        metric = AQI.calculateMetric(24, 0, 0)
        self.assertEqual(metric[0], 1)

    def test_temperature_top_good_upper(self):
        metric = AQI.calculateMetric(24.9, 0, 0)
        self.assertEqual(metric[0], 1)

    def test_temperature_top_good_boundary(self):
        metric = AQI.calculateMetric(25, 0, 0)
        self.assertEqual(metric[0], 1)

    def test_temperature_top_acceptable_lower(self):
        metric = AQI.calculateMetric(25.1, 0, 0)
        self.assertEqual(metric[0], 0.95)

    def test_temperature_top_acceptable_upper(self):
        metric = AQI.calculateMetric(26.9, 0, 0)
        self.assertEqual(metric[0], 0.05)

    def test_temperature_top_bad_boundary(self):
        metric = AQI.calculateMetric(27, 0, 0)
        self.assertEqual(metric[0], 0)

    def test_temperature_top_bad_lower(self):
        metric = AQI.calculateMetric(27.1, 0, 0)
        self.assertEqual(metric[0], -0.1)

    def test_temperature_top_bad_upper(self):
        metric = AQI.calculateMetric(27.9, 0, 0)
        self.assertEqual(metric[0], -0.9)

    def test_temperature_top_bad_dropoff(self):
        metric = AQI.calculateMetric(28, 0, 0)
        self.assertEqual(metric[0], -1)