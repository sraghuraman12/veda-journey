import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from main import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("SR"), "Hello, SR! You're on your AI journey with Veda. 🚀")
        self.assertEqual(greet("Alice"), "Hello, Alice! You're on your AI journey with Veda. 🚀")
        self.assertEqual(greet("") , "Hello, ! You're on your AI journey with Veda. 🚀")

if __name__ == "__main__":
    unittest.main()
