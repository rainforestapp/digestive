from github import Github
from datetime import datetime, timedelta

class DataPuller(object):
    def __init__(self, user, repository):
        self._user = user
        self._repoistory_name = repository
        self._gh = Github()
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repoistory_name))
        self.users = list(self._repository.get_contributors())

    def get_issues(self):
        yesterday = datetime.now() - timedelta(days=1)
        return self._repository.get_issues(sort='updated', since=yesterday)