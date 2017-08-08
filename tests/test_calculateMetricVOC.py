from unittest import TestCase
from sensors.AQI import AQI


class TestCalculateMetric(TestCase):

    def test_voc_good_bottom(self):
        metric = AQI.calculateMetric(0, 0, 1)
        self.assertEqual(metric[2], 1)

    def test_voc_good_upper(self):
        metric = AQI.calculateMetric(0, 0, 199)
        self.assertEqual(metric[2], 1)

    def test_voc_good_boundary(self):
        metric = AQI.calculateMetric(0, 0, 200)
        self.assertEqual(metric[2], 1)

    def test_voc_acceptable_lower(self):
        metric = AQI.calculateMetric(0, 0, 201)
        self.assertEqual(metric[2], 0.995)

    def test_voc_acceptable_middle(self):
        metric = AQI.calculateMetric(0, 0, 300)
        self.assertEqual(metric[2], 0.5)

    def test_voc_acceptable_upper(self):
        metric = AQI.calculateMetric(0, 0, 399)
        self.assertEqual(metric[2], 0.005)

    def test_voc_bad_lower(self):
        metric = AQI.calculateMetric(0, 0, 400)
        self.assertEqual(metric[2], 0)

    def test_voc_bad_upper(self):
        metric = AQI.calculateMetric(0, 0, 599)
        self.assertEqual(metric[2], -0.995)

    def test_voc_bad_boundary(self):
        metric = AQI.calculateMetric(0, 0, 600)
        self.assertEqual(metric[2], -1)