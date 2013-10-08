from github import Github
import requests
from collections import namedtuple
from models import DigestData
import options
from datetime import datetime, timedelta
import json
from os import path

import dateutil.parser
from template import render_collection


def main():
    try:
        opts = options.parse()
    except(options.ParseError, options.MissingArgumentError):
        print "Usage: python program.py rainforestapp/GitSatisfaction me@example.org"
        exit(1)

    digestive = Digestive(opts.username, opts.repository)
    digestive.process()


class Digestive(object):
    def __init__(self, user, repository):
        self._user = user
        self._repoistory_name = repository
        self._gh = Github()
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repoistory_name))
        self.users = list(self._repository.get_contributors())
        self._state = DigestiveState()

    def get_issues(self):
        return self._repository.get_issues(sort='updated', since=self._state.last_sent)

    def get_digest(self):
        """
        builds a DigestData instance filled with the digest
        """
        issue_list = list(self.get_issues())

        digest = DigestData()

        for issue in issue_list:
            if issue.state == IssueStates.OPEN:
                digest.total_opened += 1
            elif issue.state == IssueStates.CLOSED:
                digest.total_closed += 1

            digest.total_issues += 1

    def process(self):
        digest = self.get_issues()
        render_collection(digest)
        self._state.last_sent = datetime.now()

        self._state.save()


class IssueStates(object):
    OPEN = 'open'
    CLOSED = 'closed'


class DigestiveState(object):
    """
    Fun state stuff that needs to be saved
    """
    FILENAME = 'digestive.json'

    def __init__(self):
        if path.exists(self.FILENAME):
            self._data = json.load(open(self.FILENAME))
        else:
            self._data = {}

    @property
    def last_sent(self):
        """
        Returns the last sent time. If none exists, it defaults to the last 24 hours.
        """
        last_sent = self._data.get('last_sent')
        if last_sent:
            return dateutil.parser.parse(last_sent)
        else:
            return datetime.now() - timedelta(days=1)

    @last_sent.setter
    def last_sent(self, value):
        self._data['last_sent'] = value.isoformat()

    def save(self):
        """
        saves state to disk
        """
        json.dump(self._data, open(self.FILENAME, 'w'))


class User(object):
    def get_name(self):
        return "Simon"

    def get_gravatar(self):
        return "https://2.gravatar.com/avatar/5426390773b30a4dfee69d36f3ff9200?d=https%3A%2F%2Fidenticons.github.com%2F1a077a5cbd9f0ae7328d85157a78526d.png&s=140"


class Issue(object):
    def get_state(self):
        return "issued"

    def get_human_state(self):
        return "Issued"

    def get_title(self):
        return "Can't delete test even if not a dependency"

    def get_url(self):
        return ""

    def get_label(self):
        return "rainforestapp/turker#415"

    def get_css_class(self):
        return "opened-and-closed-issue"


class IssueCollection(object):
    def get_total_issues(self):
        return 10742

    def get_total_opened(self):
        return 5

    def get_total_closed(self):
        return 8

    def group_by_users(self):
        u1 = User()
        u1_issues = [Issue()]
        return [
            (u1, u1_issues),
            (u1, u1_issues),
        ]


if __name__ == '__main__':
    main()
