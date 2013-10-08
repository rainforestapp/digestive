import unittest

from email_template import email

class TestEmail(unittest.TestCase):
    def test_embed_html(self):
        html_file = "tests/fixtures/test.html"
        style_file = "tests/fixtures/test.css"
        output = email(open(html_file).read(), style_file)
        self.assertIn("red", output)
        
if __name__ == '__main__':
    unittest.main()
