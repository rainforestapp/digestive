import unittest

from digestive.digestive import IssueCollection
from digestive.template import render_collection

class TestTemplate(unittest.TestCase):
    def test_renders_a_collection(self):
        collection = IssueCollection()
        html = render_collection(collection)
        self.assertIn("10742", html)
        self.assertIn("5", html)

if __name__ == '__main__':
    unittest.main()
