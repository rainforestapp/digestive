from github import Github
from datetime import datetime, timedelta
import requests
import options
import argparse
import json
from os import path
import dateutil.parser

def main():
    try:
        opts = options.parse()
    except(options.ParseError, options.MissingArgumentError):
        print "Usage: python program.py rainforestapp/GitSatisfaction me@example.org"
        exit(1)

    puller = DataPuller(opts.username, opts.repository)

    print puller.users

class DataPuller(object):
    def __init__(self, user, repository):
        self._user = user
        self._repoistory_name = repository
        self._gh = Github()
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repoistory_name))
        self.users = list(self._repository.get_contributors())
        self._state = DigestiveState()

    def get_issues(self):
        return self._repository.get_issues(sort='updated', since=self._state.last_sent)

    def process(self):
        self._state.last_sent = datetime.now()



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
