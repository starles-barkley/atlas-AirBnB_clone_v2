#!/usr/bin/python3
import unittest
from models.state import State
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """ Sets up a User for testing """
        self.my_user = User()

    def test_attributes_set_to_strings(self):
        """ Checks if User attributes initialized as strings """
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "")
        self.assertEqual(self.my_user.first_name, "")
        self.assertEqual(self.my_user.last_name, "")

if __name__ == '__main__':
    unittest.main()
