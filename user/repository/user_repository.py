
from user.entity.user import User
from user.utils.file_handler import add_to_file, read_from_file


class UserRepository:
    def __init__(self, users: list[User] = None, data_file='/data/users.dat'):
        self.users = users
        self.data_file = data_file
        if not users:
            self._load()

    def exists(self,user:User) -> bool:
        return user in self.users

    def add(self,user:User) ->None:
        self.users.append(user)
        line=self._map_to_line(user)
        add_to_file(self.data_file,line)

    def _load(self):
        lines = read_from_file(self.data_file)
        users = [self._map_to_user(line) for line in lines]
        self.users = users

    def _map_to_user(self,line) -> User:
        if line and line.strip():
            username,password,token=line.strip().replace("\n","").split(" ")
            return User(username,password,token)

    def _map_to_line(self,user:User)->str:
        return f'{user.username} {user.password} {user.token}\n'


