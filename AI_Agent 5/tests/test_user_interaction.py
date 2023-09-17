
import unittest
from src import user_interaction

class TestUserInteraction(unittest.TestCase):

    def setUp(self):
        self.ui = user_interaction.UserInteraction()

    def test_handle_user_query(self):
        query = "What's the latest news?"
        response = self.ui.handle_user_query(query)
        self.assertIsNotNone(response)

    def test_send_notification(self):
        user_id = 123
        message = "New article published!"
        status = self.ui.send_notification(user_id, message)
        self.assertTrue(status)

    def test_collect_feedback(self):
        feedback = "The article was very informative."
        status = self.ui.collect_feedback(feedback)
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()

