from github import Github
from models import DigestData, Issue, User, IssueStates
import options
from mail import Mail
from mailer import Mailer
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

        digestive = Digestive(opts.username, opts.repository, opts.emails)
        digestive.process()

def get_date(closer_creater):
  if closer_creater.state == 'closed':
    return closer_creater.closed_at
  else:
    return closer_creater.created_at

class Digestive(object):
    def __init__(self, user, repository, emails):
        self._user = user
        self._repository_name = repository
        self._gh = Github(login_or_token='tals', password='Digest1ve')
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repository_name))
        self.users = list(self._repository.get_contributors())
        self._state = DigestiveState()
        self._emails = emails

    def get_pulls(self):
        pulls = list(self._repository.get_pulls(state=','.join(['open', 'closed'])))

        return sorted(pulls, key=get_date)

    def get_issues(self):
        issues = list(self._repository.get_issues(sort='updated', since=self._state.last_sent, state=','.join(['open', 'closed'])))

        return sorted(issues, key=get_date)


    def get_issues_digest(self):
        """
        builds a DigestData instance filled with the digest
        """
        issue_list = list(self.get_issues())

        digest = DigestData()
        digest.user = self._user
        digest.repo = self._repository_name

        for github_issue in issue_list:
            if github_issue.state == IssueStates.OPEN:
                digest.total_opened += 1
            elif github_issue.state == IssueStates.CLOSED:
                digest.total_closed += 1

            digest.total_issues += 1

            issue = Issue()
            issue.url = github_issue.html_url
            issue.label = '{}/{}#{}'.format(self._user, self._repository_name, github_issue.number)
            issue.title = github_issue.title
            issue.state = github_issue.state
            github_user = github_issue.user

            display_name = github_user.name or github_user.login
            if display_name not in digest.users:
                user = User()
                user.name = display_name
                user.gravatar = github_user.avatar_url
                digest.users[display_name] = user

            digest.issues.setdefault(display_name, []).append(issue)

        return digest

    def get_pulls_digest(self):
        """
        builds a DigestData instance filled with the digest
        """
        pull_list = list(self.get_pulls())

        digest = DigestData()
        digest.user = self._user
        digest.repo = self._repository_name

        for github_pull in pull_list:
            if github_pull.state == IssueStates.OPEN:
                digest.total_opened += 1
            elif github_pull.state == IssueStates.CLOSED:
                digest.total_closed += 1

            digest.total_pulls += 1

            pull = Issue()
            pull.url = github_pull.html_url
            pull.label = '{}/{}#{}'.format(self._user, self._repository_name, github_pull.number)
            pull.title = github_pull.title
            pull.state = github_pull.state
            github_user = github_pull.user

            display_name = github_user.name or github_user.login
            if display_name not in digest.users:
                user = User()
                user.name = display_name
                user.gravatar = github_user.avatar_url
                digest.users[display_name] = user

            digest.pulls.setdefault(display_name, []).append(pull)

        return digest

    def process(self):
        issues_digest = self.get_issues_digest()
        pulls_digest = self.get_pulls_digest()

        html = render_collection(issues_digest, pulls_digest)

        gmailer = Mailer(host='smtp.gmail.com', port=465, usr='username', pwd='password')

        Mail(html=html, to_emails=self._emails, from_email="test@example.org", subject="Digestive", mailer = gmailer)
        self._state.last_sent = datetime.now()

        self._state.save()



class DigestiveState(object):
    """
    Fun state stuff that needs to be saved
    """
    FILENAME = 'digestive_state.json'

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



def main():
    Cli.main()

if __name__ == '__main__':
    import os
    if path.exists(DigestiveState.FILENAME):
        os.unlink(DigestiveState.FILENAME)
    main()
