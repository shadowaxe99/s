
import unittest
from src import content_review

class TestContentReview(unittest.TestCase):

    def setUp(self):
        self.content_review = content_review.ContentReview()

    def test_review_content(self):
        ai_generated_content = "This is a sample AI generated content."
        result = self.content_review.review_content(ai_generated_content)
        self.assertIsNotNone(result)

    def test_edit_content(self):
        ai_generated_content = "This is a sample AI generated content."
        result = self.content_review.edit_content(ai_generated_content)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
