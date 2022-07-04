import unittest
from hello_world import app


class TestingCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(10, 12), 22)

    def test_multipy(self):
        self.assertEqual(app.multiply(10, 12), 120)

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
