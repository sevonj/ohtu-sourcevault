import unittest
from root import Root
from writer import Writer
from database_handler import Database
from reference import Reference
from stub_io import StubIO

class TestRoot(unittest.TestCase):
    def setUp(self):
        app_writer = Writer("test_bibtexdata.bib")
        db = Database("test_database.db")
        self.root = Root(db, app_writer, StubIO([]))

    def test_can_add_source_to_database(self):
        ref = Reference("book", "Martin09", tags=["good", "old"],
                        year="2008", title="titled",
                        author="Martti", publisher="publ")
        
        self.root.add_source(ref)
        self.root.update_database()

        # Read sources from database
        self.root.read_sources_from_database()

        read_ref = self.root.my_sources[0]

        self.assertEqual(read_ref.reference_type, "book")
        self.assertEqual(read_ref.citation_key, "Martin09")
        self.assertEqual(str(read_ref.fields.get("year")), "2008")
        self.assertEqual(read_ref.fields.get("title"), "titled")
        self.assertEqual(read_ref.fields.get("author"), "Martti")
        self.assertEqual(read_ref.fields.get("publisher"), "publ")
        self.assertEqual(read_ref.tags[0], "good")
        self.assertEqual(read_ref.tags[1], "old")