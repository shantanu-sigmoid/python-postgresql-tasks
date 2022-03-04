from cmath import exp
import unittest
import pytest
from unittest.mock import Mock
import sys
sys.path.append("../")
from models.department import Department
from models.database import Database


class TestDepartment(unittest.TestCase):
    def setUp(self):
        self.dep = Department("dd", "Alchemy", "India")
        Database.initialise(database="demo", user="postgres", password="password", host="localhost")
            
    def test_can_show_all_data(self):
        assert self.dep.show_all_data() == None

    def test_can_save_to_db(self):
        self.assertRaises(Exception, self.dep.save_to_db())
