import unittest
import options

class TestOptions(unittest.TestCase):
    def test_parse_options(self):
        opts = options.parse(["smathieu/foobar", "simon@rainforestqa.com"])
        self.assertEqual(opts.repository, 'foobar')
        self.assertEqual(opts.username, 'smathieu')
        self.assertEqual(opts.emails, ['simon@rainforestqa.com'])

    def test_parse_error(self):
        self.assertRaises(options.ParseError, options.parse, ["smathieu", "simon@rainforestqa.com"])

    def test_missing_argument(self):
        self.assertRaises(options.MissingArgumentError, options.parse, ["smathieu"])



if __name__ == '__main__':
    unittest.main()
