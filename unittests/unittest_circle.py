import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_area_float(self):
        res = circle.area(5.5)
        self.assertEqual(res, 95.03317777109123)

    def test_area_complex(self):
        res = circle.area(5j)
        self.assertEqual(res, -78.53981633974483 + 0j)

    def test_area_wrong_input(self):
        with self.assertRaises(TypeError):
            circle.area("string")

    def test_area_input_none(self):
        with self.assertRaises(TypeError):
            circle.area()

    def test_perimeter_int(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_perimeter_float(self):
        res = circle.perimeter(5.5)
        self.assertEqual(res, 34.55751918948772)

    def test_perimeter_complex(self):
        res = circle.perimeter(5j)
        self.assertEqual(res, 31.41592653589793j)

    def test_perimeter_wrong_input(self):
        with self.assertRaises(TypeError):
            circle.perimeter("string")

    def test_perimeter_input_none(self):
        with self.assertRaises(TypeError):
            circle.perimeter()
