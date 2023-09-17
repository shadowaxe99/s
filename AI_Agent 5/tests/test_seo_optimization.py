
import unittest
from src import seo_optimization

class TestSeoOptimization(unittest.TestCase):

    def setUp(self):
        self.seo = seo_optimization.SeoOptimization()

    def test_keyword_density(self):
        content = "This is a test content for SEO optimization. SEO is important for content visibility."
        result = self.seo.keyword_density(content, "SEO")
        self.assertEqual(result, 0.2)

    def test_meta_description_length(self):
        meta_description = "This is a test meta description for a test content."
        result = self.seo.meta_description_length(meta_description)
        self.assertTrue(result)

    def test_url_optimization(self):
        url = "https://www.test.com/this-is-a-test-url"
        result = self.seo.url_optimization(url)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
