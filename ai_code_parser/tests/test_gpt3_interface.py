
import unittest
from src.gpt3_interface import GPT3Interface

class TestGPT3Interface(unittest.TestCase):

    def setUp(self):
        self.gpt3 = GPT3Interface()

    def test_generate_instructions(self):
        context = "I want to combine the functionality of repo1 and repo2 to create a web application."
        instructions = self.gpt3.generate_instructions(context)
        self.assertIsInstance(instructions, str)

    def test_generate_instructions_empty_context(self):
        context = ""
        with self.assertRaises(ValueError):
            self.gpt3.generate_instructions(context)

if __name__ == '__main__':
    unittest.main()
