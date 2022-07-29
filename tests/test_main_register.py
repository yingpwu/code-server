from unittest import mock, result
from user.service.exception import UserExistsException
from user.service.user_service import UserService
from main import app, register
from user.dto.user_register_request import UserRegisterRequest

@mock.patch.object(UserService,'register',return_value=None)
@mock.patch('main.UserRepository')
def test_register_user_success(user_repository,user_service_register):
    with app.test_request_context('/register',json={'username':'fox','password':'fox123'}):
        user_service_request=UserRegisterRequest('fox','fox123')

        result=register()

        assert result == ("OK",201)
        user_service_register.aseert_called_once_with()


@mock.patch('main.UserService',**{"return_value.register.side_effect":UserExistsException})
@mock.patch('main.UserRepository')
def test_register_user_fails_with_an_exists_user(user_repository,user_service):
    with app.test_request_context('/register', json={'username': 'jack', 'password': 'jack123'}):
        user_service_request = UserRegisterRequest('jack', 'jack123')

        result = register()

        assert result == ("ERROR", 500)
        user_service.return_value.register.assert_called_once_with(user_service_request)
