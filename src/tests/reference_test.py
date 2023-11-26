import unittest
from root import Root
from writer import Writer
from database_handler import Database
from reference import Reference
from stub_io import StubIO
from bibtex_converter import convert_to_bibtex


class TestReference(unittest.TestCase):
    def setUp(self):
        self.test_ref = Reference(
            "book",
            **{
                "author": "Martti",
                "title": "titled",
                "year": "2010",
                "publisher": "publ",
            }
        )

    def test_generate_citation_key(self):
        self.assertEqual(self.test_ref.generate_citation_key(), "Martti10")

    def test_generate_citation_key_multiple_auth(self):
        test_ref2 = Reference(
            "book",
            **{
                "author": "Martti and Matti",
                "title": "titled",
                "year": "2008",
                "publisher": "publ",
            }
        )
        self.assertEqual(test_ref2.generate_citation_key(), "MM08")

    def test_str(self):
        self.test_ref.generate_citation_key()
        self.assertEqual(
            str(self.test_ref),
            ", book:\nauthor = Martti\ntitle = titled\nyear = 2010\npublisher = publ\nNo tags associated.\n",
        )

    def test_str_tags(self):
        self.test_ref.tags = ["tag1", "tag2"]
        self.assertEqual(
            str(self.test_ref),
            ", book:\nauthor = Martti\ntitle = titled\nyear = 2010\npublisher = publ\nTag 1: tag1\nTag 2: tag2\n",
        )
