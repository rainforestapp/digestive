import unittest
import digestive
from mocktest import *
from tests import MockMixin, make_mock


class TestDigestive(MockMixin, unittest.TestCase):

    @classmethod
    def make_issue(cls, state='open'):
        return make_mock(state=state)

    def test_get_digest_open_issues(self):
        digestive = Digestive('rainforestapp', 'GitSatisfaction')
        expect(digestive._repository).get_issues.and_return([self.make_issue('open')])
        digest = digestive.get_digest()

        self.assertEqual(digest.total_opened, 1)
        self.assertEqual(digest.total_closed, 0)
        self.assertEqual(digest.total_issues, 1)

    def test_get_digest_closed_issues(self):
        digestive = Digestive('rainforestapp', 'GitSatisfaction')
        expect(digestive._repository).get_issues.and_return([self.make_issue('closed')])
        digest = digestive.get_digest()

        self.assertEqual(digest.total_opened, 0)
        self.assertEqual(digest.total_closed, 1)
        self.assertEqual(digest.total_issues, 1)


if __name__ == '__main__':
    unittest.main()
