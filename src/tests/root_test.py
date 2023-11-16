import unittest
from root import Root
from source_stub import SourceStub

class TestRoot(unittest.TestCase):
    def setUp(self):
        self.root_stub = Root(SourceStub())

    def test_search(self):
        self.assertAlmostEqual(self.root_stub.my_sources[0], 'Kirjailija_0')
    