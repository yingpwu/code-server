from user.dto.user_register_request import UserRegisterRequest


def test_create_user_register_request_with_username_and_pssword():
    user_register_request = UserRegisterRequest(
        username="User", password='User123')

    assert user_register_request is not None
    assert user_register_request.username == "User"
    assert user_register_request.password == "User123"
