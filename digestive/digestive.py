from github import Github
from models import DigestData
import options
from mail import Mail
from datetime import datetime, timedelta
import json
from os import path

import dateutil.parser
from template import render_collection

class Cli(object):
    @classmethod
    def main(self):
        try:
            opts = options.parse()
        except(options.ParseError, options.MissingArgumentError):
            print "Usage: digestive rainforestapp/digestive me@example.org"
            exit(1)

        print "Xxx"
        digestive = Digestive(opts.username, opts.repository, opts.emails)
        digestive.process()


class Digestive(object):
    def __init__(self, user, repository, emails):
        self._user = user
        self._repoistory_name = repository
        self._gh = Github(login_or_token='tals', password='Digest1ve')
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repoistory_name))
        self.users = list(self._repository.get_contributors())
        self._state = DigestiveState()
        self._emails = emails

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

        return digest

    def process(self):
        digest = self.get_issues()
        Mail(html=render_collection(digest), to_emails=self._emails, from_email='test@example.org', subject="Digestive")
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



def main():
    Cli.main()

if __name__ == '__main__':
    main()
