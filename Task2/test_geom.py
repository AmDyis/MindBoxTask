import unittest
from GeomFigures import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.get_right_triangle())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.get_right_triangle())

    def test_calculate_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == '__main__':
    unittest.main()
