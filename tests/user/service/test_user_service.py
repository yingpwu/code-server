
from unittest import mock
from user.dto.user_register_request import UserRegisterRequest
from user.repository.user_repository import UserRepository
from user.service.exception import UserExistsException
from user.service.user_service import UserService
from user.entity.user import User


def test_register_success_with_a_new_user():
    user_repository=mock.create_autospec(UserRepository)
    user_repository.add.return_value=None
    user_repository.exists.return_value=False

    user_service=UserService(user_repository)
    user_register_request=UserRegisterRequest('fox','fox123')
    user=User('fox','fox123')

    user_service.register(user_register_request)
    user_repository.add.assert_called_once_with(user)
    user_repository.exists.assert_called_once_with(user)

def test_register_fails_with_an_exists_user():
    user_repository = mock.create_autospec(UserRepository)
    user_repository.add.return_value = None
    user_repository.exists.return_value = True

    user_service= UserService(user_repository)
    user_service = UserService(user_repository)
    user_register_request = UserRegisterRequest('rose', 'rose123')
    user = User('rose', 'rose123')

    try:
        user_service.register(user_register_request)
    except UserExistsException:
        pass

    user_repository.exists.assert_called_once_with(user)
    user_repository.add.assert_not_called()