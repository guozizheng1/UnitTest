import unittest
from app.utils.calculator import add


class TestCalculate(unittest.TestCase):
    def test_add_method(self):
        self.assertEqual(7, add(3, 4))

if __name__ == '__main__':
    unittest.main()
