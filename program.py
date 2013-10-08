from github import Github
from datetime import datetime, timedelta
import requests
def main():
    puller = DataPuller('rainforestapp', 'GitSatisfaction')
    print puller.users

def main3():
    gh = Github()
    repo = gh.get_repo('rainforestapp/GitSatisfaction')
    for issue in repo.get_issues():
        print issue.title, issue.state, issue.labels, issue.body


class DataPuller(object):
    def __init__(self, user, repository):
        self._user = user
        self._repoistory_name = repository
        self._gh = Github()
        self._repository = self._gh.get_repo("{}/{}".format(self._user, self._repoistory_name))
        self.users = list(self._repository.get_contributors())

    def get_issues(self):
        yesterday = datetime.now() - timedelta(days=1)
        return self._repoistory_name.get_issues(sort='updated', since=yesterday)

    def commits(self):
        pass
    
if __name__ == '__main__':
    main()