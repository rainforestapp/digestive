class DigestData(object):
    def __init__(self):
        self.total_issues = 0
        self.total_opened = 0
        self.total_closed = 0

    @property
    def group_by_users(self):
        return []


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

