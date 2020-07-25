import math
import unittest

from answer import Circle


class CircleTest(unittest.TestCase):
    def test_area(self):
        radius = 2
        c = Circle(radius)

        self.assertEqual(c.area(), math.pi * radius ** 2)

    def test_perimeter(self):
        radius = 3
        c = Circle(radius)
        self.assertEqual(c.perimeter(), 2 * math.pi * radius)

    def test_failure(self):
        with self.assertRaises(ValueError):
            c = Circle(-1)


if __name__ == '__main__':
    unittest.main()
