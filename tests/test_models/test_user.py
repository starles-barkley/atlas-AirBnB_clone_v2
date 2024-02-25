#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """ Tests the user class """

    def test_is_first_name_a_string(self):
        """ Tests if the type of first_name is a string """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_is_last_name_a_string(self):
        """ Checks if type of last_name is a string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_is_email_a_string(self):
        """ Checks if type of email is a string """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_is_password_a_string(self):
        """ Checks if type of password is a string """
        new = self.value()
        self.assertEqual(type(new.password), str)
