from cmath import exp
import unittest
import pytest
from unittest.mock import Mock
import sys
sys.path.append("../")
from models.employee import Employee
from models.database import Database


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("dd", "Alchemy", "India", "demo", "demo", "demo", "demo", "demo")
        Database.initialise(database="demo", user="postgres", password="password", host="localhost")
            
    def test_can_show_all_data(self):
        assert self.emp.show_all_data() == None

    def test_can_save_to_db(self):
        self.assertRaises(Exception, self.emp.save_to_db())
