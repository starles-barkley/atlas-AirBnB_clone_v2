#!/usr/bin/python3
"""Unit tests for DBStorage"""

import os
import unittest
import pycodestyle
from models import storage
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv("HBNB_ENV") != "db", 'DBStorage inactive')
class TestDBStorageClass(unittest.TestCase):
    """Test cases for DBStorage class"""

    def test_class_doc_string(self):
        """Test docstring for the class"""
        self.assertTrue(len(DBStorage.__doc__) > 0)

    def test_all_method_doc_string(self):
        """Test docstring for the all() method"""
        self.assertTrue(len(DBStorage.all.__doc__) > 0)

    def test_new_method_doc_string(self):
        """Test docstring for the new() method"""
        self.assertTrue(len(DBStorage.new.__doc__) > 0)

    def test_save_method_doc_string(self):
        """Test docstring for the save() method"""
        self.assertTrue(len(DBStorage.save.__doc__) > 0)

    def test_reload_method_doc_string(self):
        """Test docstring for the reload() method"""
        self.assertTrue(len(DBStorage.reload.__doc__) > 0)

    def test_delete_method_doc_string(self):
        """Test docstring for the delete() method"""
        self.assertTrue(len(DBStorage.delete.__doc__) > 0)

    def test_pycodestyle(self):
        """Test compliance with PEP 8"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/engine/db_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_call_with_argument(self):
        """Make sure that TypeError is raised when argument is supplied"""
        with self.assertRaises(TypeError):
            DBStorage(1)

    def test_engine_type(self):
        """Test that __engine attribute is of correct type"""
        self.assertEqual(type(storage._DBStorage__engine), Engine)

    def test_session_type(self):
        """Test that __session attribute is of correct type"""
        self.assertEqual(type(storage._DBStorage__session), Session)

    def test_engine_private(self):
        """Test that __engine attribute is private"""
        with self.assertRaises(AttributeError):
            print(storage.__engine)

    def test_session_private(self):
        """Test that __session attribute is private"""
        with self.assertRaises(AttributeError):
            print(storage.__session)

    def test_type(self):
        """Verify that type returns correct object type"""
        db = DBStorage()
        self.assertTrue(type(db) is DBStorage)


if __name__ == "__main__":
    unittest.main()
