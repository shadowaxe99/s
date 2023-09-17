
import unittest
from src import content_curation

class TestContentCuration(unittest.TestCase):

    def setUp(self):
        self.curator = content_curation.ContentCurator()

    def test_curate_content(self):
        content = "This is a sample news content."
        result = self.curator.curate_content(content)
        self.assertIsNotNone(result)

    def test_filter_content(self):
        content = ["news1", "news2", "news3"]
        result = self.curator.filter_content(content)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()

