from collections import namedtuple


class DigestData(object):
    def __init__(self):
        self.total_issues = 0
        self.total_opened = 0
        self.total_closed = 0
        self.issues = {}

    @property
    def group_by_users(self):
        issues = self.issues.items()
        issues.sort(cmp=lambda x: x[0].name)

        return issues

class Issue(object):
    def __init__(self):
        self.state = None
        self.human_state = None
        self.url = None
        self.label = None
        self.css_class = None
        self.title = None



class User(object):
    def __init__(self):
        self.name = None
        self.gravatar = None

