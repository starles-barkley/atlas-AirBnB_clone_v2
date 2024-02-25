#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """ Tests the user class """

    def __init__(self, *args, **kwargs):
        """  """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Tests if the type of first_name is a string """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Checks if type of last_name is a string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Checks if type of email is a string """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Checks if type of password is a string """
        new = self.value()
        self.assertEqual(type(new.password), str)
