from user.dto.user_register_request import UserRegisterRequest
from user.repository.user_repository import UserRepository
from user.entity.user import User
from user.service.exception import UserExistsException

class UserService():
    def __init__(self,user_repository:UserRepository) -> None:
        self.user_repository=user_repository


    def register(self,user_register_reuest:UserRegisterRequest):
        # 1.dto -> entity
        user = User(user_register_reuest.username,user_register_reuest.password)
        # 2. 检测用户是否存在
        if self.user_repository.exists(user):
            # 2.1 用户存在
            #   抛出错误
            raise UserExistsException(f'用户{user.username}已经存在,不可重复注册')
        
        # 2.2 用户不存在
        #   新增用户
        self.user_repository.add(user)