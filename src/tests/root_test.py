import unittest
from root import Root
from source_stub import SourceStub
from writer import Writer

class TestRoot(unittest.TestCase):
    def setUp(self):
        app_writer = Writer("data.bib")
        self.root_stub = Root(app_writer)

        for book in SourceStub():
            self.root_stub.my_sources.append(book)


    def test_CheckKirjailija(self):
        lista = self.root_stub.my_sources

        
        source = lista[1]
        self.assertEqual(str(source), 'Kirjailija_1. Kirja_1.\nJulkaisija_1, 1')
        
    