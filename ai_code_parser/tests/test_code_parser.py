
import unittest
from src.code_parser import CodeParser

class TestCodeParser(unittest.TestCase):

    def setUp(self):
        self.parser = CodeParser()

    def test_parse_repo(self):
        repo_path = "data/repos/repo1"
        result = self.parser.parse_repo(repo_path)
        self.assertIsInstance(result, dict)

    def test_merge_code(self):
        repo1_path = "data/repos/repo1"
        repo2_path = "data/repos/repo2"
        result = self.parser.merge_code(repo1_path, repo2_path)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
