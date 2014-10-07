from collections import namedtuple


class DigestData(object):
    def __init__(self, item_type):
        self.item_type = item_type
        self.total_items = 0
        self.total_opened = 0
        self.total_closed = 0
        self.user = None
        self.repo = None
        self.items = {}
        self.users = {}

    @property
    def group_by_users(self):
        items = [(self.users[k], v) for k, v in self.items.items()]
        items.sort(key=lambda x: x[0].name)

        return items

    @property
    def closed_url(self):
      return self.unfiltered_url + "?state=closed"

    @property
    def opened_url(self):
      return self.unfiltered_url + "?state=open"

    @property
    def unfiltered_url(self):
      return "https://github.com/%s/%s/%s" % (self.user, self.repo, self.item_type, )

class Item(object):
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
        if self.state == ItemStates.CLOSED:
            return 'closed-issue'
        else:
            return 'opened-issue'

class User(object):
    def __init__(self):
        self.name = None
        self.gravatar = None


class ItemStates(object):
    OPEN = 'open'
    CLOSED = 'closed'
