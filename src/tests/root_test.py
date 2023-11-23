import unittest
from root import Root
from writer import Writer
from database_handler import Database

class TestRoot(unittest.TestCase):
    def setUp(self):
        app_writer = Writer("data.bib")
        db = Database("database.db")
        self.root_stub = Root(db, app_writer)

    def test_CheckKirjailija(self):
        lista = self.root_stub.my_sources

        self.assertEqual("abc", "abc")