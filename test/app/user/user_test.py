import unittest
from app.user.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.u = User('Tom', 'test@gmail.com', '123456')
        self.users = [self.u, User('Jerry', 'test@gmail.com', '654321')]

    def test_add_method(self):
        # u = User('Tom', 'test@gmail.com', '123456')
        self.assertEqual(6, self.u.add(3, 3))

    def test_user_is_vaild(self):
        # u = User('Jerry', 'test@gmail.com', '123456')
        # self.assertEqual(True, u.user_is_valid('Jerry', '123456'))
        self.assertTrue(self.u.user_is_valid('Tom', '123456'))

    def test_user_in(self):
        self.assertIn(self.u, self.users)

if __name__ == '__main__':
    unittest.main()