import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area_int(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_area_float(self):
        res = square.area(5.5)
        self.assertEqual(res, 30.25)

    def test_area_complex(self):
        res = square.area(5j)
        self.assertEqual(res, -25+0j)

    def test_area_wrong_input(self):
        with self.assertRaises(TypeError):
            square.area("string")

    def test_area_input_none(self):
        with self.assertRaises(TypeError):
            square.area()

    def test_perimeter_int(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_float(self):
        res = square.perimeter(5.5)
        self.assertEqual(res, 22)

    def test_perimeter_complex(self):
        res = square.perimeter(5j)
        self.assertEqual(res, 20j)

    def test_perimeter_wrong_input(self):
        with self.assertRaises(TypeError):
            square.perimeter("string")

    def test_perimeter_input_none(self):
        with self.assertRaises(TypeError):
            square.perimeter()
