import unittest

from data_puller import IssueCollection
from template import render_collection

class TestTemplate(unittest.TestCase):
    def test_renders_a_collection(self):
        collection = IssueCollection()
        html = render_collection(collection)
        self.assertIn("10742", html)
        self.assertIn("5", html)

if __name__ == '__main__':
    unittest.main()
