#!/usr/bin/python3
"""Tests for BaseModel class"""

import os
import unittest
import pycodestyle
from models.base_model import BaseModel
from models import storage
from genericpath import exists


class TestBaseModelInitialization(unittest.TestCase):
    """Tests for BaseModel initialization"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before the first test"""
        cls.model1 = BaseModel()
        cls.model2 = BaseModel()
        cls.model3 = BaseModel(**cls.model1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.model1
        del cls.model2
        del cls.model3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_docstring(self):
        """Test if module docstring is present"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_init_docstring(self):
        """Test if __init__ method docstring is present"""
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)

    def test_str_docstring(self):
        """Test if __str__ method docstring is present"""
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)

    def test_save_docstring(self):
        """Test if save method docstring is present"""
        self.assertTrue(len(BaseModel.save.__doc__) > 0)

    def test_to_dict_docstring(self):
        """Test if to_dict method docstring is present"""
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    def test_delete_docstring(self):
        """Test if delete method docstring is present"""
        self.assertTrue(len(BaseModel.delete.__doc__) > 0)


    def test_pycodestyle(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/base_model.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_id_initialization(self):
        """Test initialization of id attribute"""
        self.assertTrue(self.model1.id, exists)
        self.assertTrue(self.model2.id, exists)
        self.assertTrue(isinstance(self.model1.id, str))
        self.assertTrue(isinstance(self.model2.id, str))
        self.assertEqual(len(self.model1.id), 36)
        self.assertEqual(len(self.model2.id), 36)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_created_at_initialization(self):
        """Test initialization of created_at attribute"""
        self.assertTrue(self.model1.created_at, exists)
        self.assertTrue(self.model2.created_at, exists)
        self.assertNotEqual(self.model1.created_at, self.model2.created_at)

    def test_updated_at_initialization(self):
        """Test initialization of updated_at attribute"""
        self.assertTrue(self.model1.updated_at, exists)
        self.assertTrue(self.model2.updated_at, exists)
        self.assertEqual(self.model1.created_at, self.model1.updated_at)
        self.assertEqual(self.model2.created_at, self.model2.updated_at)
        self.assertNotEqual(self.model1.updated_at, self.model2.updated_at)

    def test_init_kwargs_direct(self):
        """Test initialization with kwargs directly"""
        kwargs_model = BaseModel(id=2147483647)
        self.assertEqual(kwargs_model.id, 2147483647)

    def test_init_args(self):
        """Test that random arguments as args are not recorded"""
        args_model = BaseModel([2, 4, 8, 16])
        self.assertNotIn('[2, 4, 8, 16]', args_model.__dict__.items())

    def test_type(self):
        """Test type returns correct object type"""
        self.assertTrue(isinstance(self.model1, BaseModel))


class TestBaseModelStringRepresentation(unittest.TestCase):
    """Tests for BaseModel string representation"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before the first test"""
        cls.model1 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.model1

    def test_base_model_str(self):
        """Test correct object string representation"""
        expected_str = "[{}] ({}) {}".format(
            self.model1.__class__.__name__,
            self.model1.id,
            self.model1.__dict__,
        )
        self.assertEqual(str(self.model1), expected_str)
        self.assertEqual(self.model1.__str__(), expected_str)


@unittest.skipIf(os.getenv("HBNB_ENV") is not None, 'FileStorage inactive')
class TestBaseModelSaveMethod(unittest.TestCase):
    """Tests for BaseModel save method"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before the first test"""
        cls.model1 = BaseModel()
        cls.model1.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.model1

    def test_save_with_argument(self):
        """Test save method raises TypeError when argument supplied"""
        with self.assertRaises(TypeError):
            self.model1.save(1)

    def test_save(self):
        """Test BaseModel save method correct operation"""
        self.assertNotEqual(self.model1.updated_at, self.model1.created_at)
        self.assertTrue(self.model1.created_at < self.model1.updated_at)


class TestBaseModelToDictMethod(unittest.TestCase):
    """Tests for BaseModel to_dict method"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before the first test"""
        cls.model1 = BaseModel()
        cls.model1_dict = cls.model1.to_dict()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.model1

    def test_to_dict_with_argument(self):
        """Test to_dict method raises TypeError when argument supplied"""
        with self.assertRaises(TypeError):
            self.model1.to_dict(1)

    def test_to_dict_success(self):
        """Test object dictionary initialized and of dict type"""
        self.assertTrue(self.model1_dict, exists)
        self.assertTrue(isinstance(self.model1_dict, dict))

    def test_to_dict_keys(self):
        """Test to_dict correctly collects obj attributes into keys"""
        self.assertIn('__class__', self.model1_dict)
        self.assertIn('created_at', self.model1_dict)
        self.assertIn('updated_at', self.model1_dict)
        self.assertIn('id', self.model1_dict)

    def test_to_dict_values(self):
        """Test to_dict matches attribute values to correct dict keys"""
        self.assertEqual(self.model1_dict['__class__'], 'BaseModel')
        self.assertEqual(
            self.model1_dict['__class__'],
            self.model1.__class__.__name__
        )
        self.assertEqual(
            self.model1_dict['created_at'],
            self.model1.created_at.isoformat()
        )
        self.assertEqual(
            self.model1_dict['updated_at'],
            self.model1.updated_at.isoformat()
        )
        self.assertEqual(self.model1_dict['id'], self.model1.id)


@unittest.skipIf(os.getenv("HBNB_ENV") is not None, 'FileStorage inactive')
class TestBaseModelDeleteMethod(unittest. TestCase):
    """Tests for BaseModel delete method"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before the first test"""
        cls.model1 = BaseModel()
        cls.model1.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.model1

    def test_delete(self):
        """Test BaseModel delete method correct operation"""
        mod1_id = f'{self.model1.__class__.__name__}.{self.model1.id}'
        self.assertIn(mod1_id, storage._FileStorage__objects)
        self.assertIn(self.model1, storage._FileStorage__objects.values())
        self.model1.delete()
        self.assertNotIn(mod1_id, storage._FileStorage__objects)
        self.assertNotIn(mod1_id, storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
