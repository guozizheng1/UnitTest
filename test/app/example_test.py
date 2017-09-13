import unittest


class TestExample(unittest.TestCase):
    # 判断是否相等
    def test_assert_equal(self):
        self.assertEqual(1, 1)

    # 判断约等于
    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1, 1.5, delta=0.5)

    # 判断是否大于
    def test_assert_greater(self):
        self.assertGreater(2, 1)

if __name__ == '__main__':
    unittest.main()
