import unittest


class TestExample(unittest.TestCase):
    # 判断是否相等
    def test_assert_equal(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
