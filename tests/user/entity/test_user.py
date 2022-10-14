from user.entity.user import User
from unittest import mock

def test_create_a_user():
    user = User('User', 'User123')

    assert user is not None
    assert user.username=="User"
    assert user.password=="User123"


def test_create_a_new_user_with_given_username_and_password():
    username = 'User'
    password = 'User123'

    user = User(username=username, password=password)

    assert user.username == username
    assert user.password == password


def test_user_identified_with_only_username():
    user1 = User('User', 'User123')
    user2 = User('User', 'User123')

    assert user1 == user2
    assert user1.username == user2.username


def test_user_should_have_the_token_atrribute():
    user = User('User', 'User123')

    # user.token = '123adc'

    assert user.token is not None


@mock.patch('user.entity.user.encode')
def test_token_should_be_built_when_initialize_the_user(encode):

    GIVEN_TOKEN = 'xxxzzz'
    encode.return_value=GIVEN_TOKEN
    user = User('User', 'User123')

    assert user.token == GIVEN_TOKEN
