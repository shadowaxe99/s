
import unittest
from src import publishing_automation

class TestPublishingAutomation(unittest.TestCase):

    def setUp(self):
        self.publishing_automation = publishing_automation.PublishingAutomation()

    def test_schedule_post(self):
        result = self.publishing_automation.schedule_post("Test Title", "Test Content", "2022-12-31 23:59")
        self.assertEqual(result, True)

    def test_publish_now(self):
        result = self.publishing_automation.publish_now("Test Title", "Test Content")
        self.assertEqual(result, True)

    def test_delete_scheduled_post(self):
        result = self.publishing_automation.delete_scheduled_post(1)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

