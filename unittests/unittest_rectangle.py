import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = rectangle.area(5, 6)
        self.assertEqual(res, 30)

    def test_area_float(self):
        res = rectangle.area(5.5, 6.5)
        self.assertEqual(res, 35.75)

    def test_area_complex(self):
        res = rectangle.area(5j, 6j)
        self.assertEqual(res, -30+0j)

    def test_area_wrong_input(self):
        with self.assertRaises(TypeError):
            rectangle.area("string", "string")

    def test_area_input_none(self):
        with self.assertRaises(TypeError):
            rectangle.area()

    def test_perimeter_int(self):
        res = rectangle.perimeter(5, 6)
        self.assertEqual(res, 22)

    def test_perimeter_float(self):
        res = rectangle.perimeter(5.5, 6.5)
        self.assertEqual(res, 24)

    def test_perimeter_complex(self):
        res = rectangle.perimeter(5j, 6j)
        self.assertEqual(res, 22j)

    def test_perimeter_wrong_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("string", "string")

    def test_perimeter_input_none(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter()