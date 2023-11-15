import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = triangle.area(5, 6)
        self.assertEqual(res, 15)

    def test_area_float(self):
        res = triangle.area(5.5, 6.5)
        self.assertEqual(res, 17.875)

    def test_area_complex(self):
        res = triangle.area(5j, 6j)
        self.assertEqual(res, -15+0j)

    def test_area_wrong_input(self):
        with self.assertRaises(TypeError):
            triangle.area("string", "string")

    def test_area_input_none(self):
        with self.assertRaises(TypeError):
            triangle.area()

    def test_perimeter_int(self):
        res = triangle.perimeter(5, 6, 7)
        self.assertEqual(res, 18)

    def test_perimeter_float(self):
        res = triangle.perimeter(5.5, 6.5, 7.5)
        self.assertEqual(res, 19.5)

    def test_perimeter_complex(self):
        res = triangle.perimeter(5j, 6j, 7j)
        self.assertEqual(res, 18j)

    def test_perimeter_wrong_input(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("string", "string", "string")

    def test_perimeter_input_none(self):
        with self.assertRaises(TypeError):
            triangle.perimeter()