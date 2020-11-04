#!/usr/bin/python3
"""Unittest for BaseModel()
"""
import unittest
from models.base_model import BaseModel


class Test_attributes(unittest.TestCase):
    """ Tests for base model attributes """
    def Test_id_type(self):
        """ test id """
        self.assertEqual(type(self.id), str)

    def test_created_at(self):
        """test created_at"""
        x = BaseModel().to_dict()
        self.assertEqual(type(self.created_at), datetime.datetime)
        self.assertEqual(type(x.created_at), str)

    def test_updated_at(self):
        """test updated_at"""
        x = BaseModel().to_dict()
        self.assertEqual(type(self.updated_at), datetime.datetime)
        self.assertEqual(type(x.updated_at), str)

if __name__ == '__main__':
    unittest.main()
