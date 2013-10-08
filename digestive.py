from github import Github
import options
from github import Github
from datetime import datetime, timedelta
import options
import json
from os import path

import dateutil.parser

def main():
    try:
        opts = options.parse()
    except(options.ParseError, options.MissingArgumentError):
        print "Usage: python program.py rainforestapp/GitSatisfaction me@example.org"
        exit(1)

    digestive = Digestive(opts.username, opts.repository)

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


class IssueCollection(object):
    def total_issues(self):
        return 10742

    def total_opened(self):
        return 5
    
    def total_closed(self):
        return 8

if __name__ == '__main__':
    main()
