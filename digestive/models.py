from collections import namedtuple


class DigestData(object):
    def __init__(self):
        self.total_issues = 0
        self.total_opened = 0
        self.total_closed = 0
        self.issues = {}
        self.users = {}

    @property
    def group_by_users(self):
        issues = [(self.users[k], v) for k, v in self.issues.items()]
        issues.sort(key=lambda x: x[0].name)

        return issues

class Issue(object):
    def __init__(self):
        self.state = None
        self.url = None
        self.label = None
        self.title = None

    @property
    def human_state(self):
        return self.state.capitalize()

    @property
    def css_class(self):
        if self.state == IssueStates.CLOSED:
            return 'closed-issue'
        else:
            return 'opened-issue'

class User(object):
    def __init__(self):
        self.name = None
        self.gravatar = None


class IssueStates(object):
    OPEN = 'open'
    CLOSED = 'closed'
