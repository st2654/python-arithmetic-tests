import unittest

from geometry import area_rectangle, perimeter_rectangle


class GeometryTests(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area_rectangle(3, 4), 12)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter_rectangle(3, 4), 14)
