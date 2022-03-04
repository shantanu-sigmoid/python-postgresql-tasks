from argparse import ArgumentError
import unittest

import sys
sys.path.append("../")
from models.database import CursorFromConnectionPool, Database, Engine


class TestClass(unittest.TestCase):
    def setUp(self):
        self.db = Database
        self.cursor = CursorFromConnectionPool()
        self.engine = Engine("demo")

    def test_can_instantiate_database(self):
        self.assertTrue(Database.initialise)
    
    def test_can_get_connection(self):
        self.assertTrue(Database.get_connection)
    
    def test_can_get_cursor_from_connection_pool(self):
        self.assertTrue(self.cursor.__enter__)
    
    def test_can_make_engine(self):
        self.assertRaises(TypeError, self.engine.make_engine())