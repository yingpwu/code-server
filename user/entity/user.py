from user.utils.jwt import encode

class User():
    def __init__(self,username=None,password=None):
        self.username=username
        self.password=password
        self._build_token()
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username ==other.username

    def _build_token(self):
        if self.username:
            payload={'username':self.username}
            self.token=encode(payload)