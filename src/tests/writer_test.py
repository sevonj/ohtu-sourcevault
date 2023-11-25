import unittest
from writer import Writer
from reference import Reference

class TestWriter(unittest.TestCase):
    def setUp(self):
        self.app_writer = Writer("test_bibtexdata.bib")
        self.test_ref = Reference("book", **{"author":"Martti", "title":"titled","year":"2008","publisher":"publ"})
        
    def test_reads_and_writes_data_in_file(self):
        # Writing test reference to test_bibtexdata.bib
        self.app_writer.write_all_to_file([self.test_ref])

        # Reading the created file
        file = self.app_writer.read_from_file()

        # Checking that the created data is readable and intact
        self.assertEqual(file[0].fields.get("title"),"titled")