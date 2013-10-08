import json


class Config(object):
    def __init__(self, filename):
        self._data = json.load(open(filename))

    @property
    def emails(self):
        return self._data.get('emails', [])

    def auth_username(self):
        """
        Username for authentication
        """
        return self._data.get('username')

    def auth_password(self):
        """
        The password. Optional. Only used for private repositories.
        """
        return self._data.get('password')

    def repository(self):
        """
        The repository to process. Of username/repository form.
        """
        return self._data['repository']
