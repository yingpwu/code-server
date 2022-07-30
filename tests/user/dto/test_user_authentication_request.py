from unittest import mock
from user.dto.user_authentication_request import UserAuthenticationRequest
from user.entity.user import User


def test_user_success_create_authentication_request_with_username_and_password():
    username, password = 'jack', 'jack123'
    user_authentication_request = UserAuthenticationRequest(username, password)

    assert user_authentication_request.username == username
    assert user_authentication_request.password == password


def test_user_authentication_request_should_equals_with_the_same_attributes():
    username, password = 'jack', 'jack123'
    user_authentication_request1 = UserAuthenticationRequest(
        username, password)
    user_authentication_request2 = UserAuthenticationRequest(
        username, password)

    assert user_authentication_request1 == user_authentication_request2

