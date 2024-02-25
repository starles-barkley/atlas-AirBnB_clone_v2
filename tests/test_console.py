#!/usr/bin/python3

import unittest
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def test_quit(self):
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

if __name__ == '__main__':
    unittest.main()