from unittest import mock
import pytest
from user.entity.user import User
from user.repository.user_repository import UserRepository


@pytest.fixture
def lines():
    return [
        'coder coder123\n',
        'jack jack123\n',
        'rose rose123\n',
        'albert albert123\n',
        'david david123\n'

    ]


@pytest.fixture
def users():
    user1 = User('coder', 'coder123')
    user2 = User('jack', 'jack123')
    user3 = User('rose', 'rose123')
    user4 = User('albert', 'albert123')
    user5 = User('david', 'david123')

    users = [user1, user2, user3, user4, user5]
    return users


def test_initialize_with_given_users(users):
    user_repository = UserRepository(users)

    assert user_repository.users == users


@mock.patch('user.repository.user_repository.read_from_file')
def test_initialize_with_given_file(read_from_file, users, lines):
    read_from_file.return_value = lines

    user_repository = UserRepository(data_file='/data/users.dat')

    assert user_repository.users == users
    read_from_file.assert_called_once_with('/data/users.dat')


@mock.patch('user.repository.user_repository.read_from_file')
def test_check_user_exists(read_from_file, lines, users):
    read_from_file.return_value = lines
    user_repository = UserRepository()
    user = User('coder', 'coder123')
    not_exists_user = User('User', 'User123')

    assert user_repository.exists(user) is True
    assert user_repository.exists(not_exists_user) is False
    read_from_file.assert_called_once_with('/data/users.dat')


@mock.patch('user.repository.user_repository.read_from_file')
@mock.patch('user.repository.user_repository.add_to_file')
def test_add_a_new_user(add_to_file, read_from_file, lines):
    read_from_file.return_value = lines
    user_repository = UserRepository()
    a_new_user = User('alex', 'alex123')

    user_repository.add(a_new_user)

    assert a_new_user in user_repository.users
    add_to_file.assert_called_once_with('/data/users.dat','alex alex123\n')