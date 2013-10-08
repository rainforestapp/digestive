import unittest
from digestive import Digestive
from mocktest import *
from tests import MockMixin


class MyTestCase(MockMixin, unittest.TestCase):
    def test_something(self):
        from github import Github
        puller = Digestive('rainforestapp', 'GitSatisfaction')
        expect(puller._repository).get_issues.and_return(['1', '2', '3'])
        self.assertListEqual(puller.get_issues(), ['1', '2', '3'])

if __name__ == '__main__':
    unittest.main()
