
from readline import write_history_file
from user.entity.user import User
from user.utils.file_handler import add_to_file, read_from_file, write_to_file


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

    def find(self,username:str,password:str)->User:
        self._load()
        for user in self.users:
            if user.username==username and user.password==password:
                return User(username=username,password=password)
            else:
                return None
    
    def update(self, user: User) -> None:
        for original_user in self.users:
            if original_user.username==user.username:
                original_user.password=user.password
                original_user.token=user.token
                self._refresh(self.users,self.data_file)
                
    @classmethod
    def _refresh(cls,users,path):
        user_lines=[f'{user.username} {user.password} {user.token}' for user in users]
        write_to_file(path, user_lines)

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


