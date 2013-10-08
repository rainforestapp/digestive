import unittest
from digestive.models import DigestData

from digestive.template import render_collection

class TestTemplate(unittest.TestCase):
    def test_renders_a_collection(self):
        digest = DigestData()
        digest.total_issues = 10742
        digest.total_closed = 5

        html = render_collection(digest)
        self.assertIn("10742", html)
        self.assertIn("5", html)

if __name__ == '__main__':
    unittest.main()
