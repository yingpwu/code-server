from unittest import mock
import pytest
from user.entity.user import User
from user.repository.user_repository import UserRepository


@pytest.fixture
def lines():
    return [
        'coder coder123 code_fake_token\n',
        'jack jack123 jack_fake_token\n',
        'rose rose123 rose_fake_token\n',
        'albert albert123 albert_fake_token\n',
        'david david123 david_fake_token\n'

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


@mock.patch('user.entity.user.encode')
@mock.patch('user.repository.user_repository.read_from_file')
@mock.patch('user.repository.user_repository.add_to_file')
def test_add_a_new_user(add_to_file, read_from_file, encode, lines):
    encode.return_value = 'fake_token'
    read_from_file.return_value = lines
    user_repository = UserRepository()
    a_new_user = User('alex', 'alex123')

    user_repository.add(a_new_user)

    assert a_new_user in user_repository.users
    add_to_file.assert_called_once_with(
        '/data/users.dat', 'alex alex123 fake_token\n')


@mock.patch('user.entity.user.encode')
@mock.patch('user.repository.user_repository.read_from_file')
@mock.patch('user.repository.user_repository.add_to_file')
def test_should_persistent_authentication(add_to_file, read_from_file, encode, lines):
    read_from_file.return_value = lines
    encode.return_value = 'fake_token'
    user_repository = UserRepository()
    a_new_user = User('alex', 'alex123')

    user_repository.add(a_new_user)

    assert a_new_user in user_repository.users
    assert a_new_user.token is not None
    add_to_file.assert_called_once_with(
        '/data/users.dat', 'alex alex123 fake_token\n')


@mock.patch('user.entity.user.encode')
@mock.patch('user.repository.user_repository.read_from_file')
@mock.patch('user.repository.user_repository.add_to_file')
def test_should_persistent_authentication(add_to_file, read_from_file, encode, lines, users):
    read_from_file.return_value = lines
    user_repository = UserRepository()

    coder = User('coder', 'coder123', 'coder_fake_token')

    assert coder in user_repository.users
    assert users == user_repository.users


@mock.patch('user.repository.user_repository.read_from_file')
def test_should_find_user_with_username_and_password(read_from_file, lines, users):
    read_from_file.return_value = lines
    username = 'coder'
    password = 'coder123'

    user_repository = UserRepository(users)
    user_found = user_repository.find(username, password)

    assert user_found is not None
    assert user_found.username == username
    assert user_found.password == password
    read_from_file.assert_called_once()


@mock.patch('user.repository.user_repository.read_from_file')
def test_not_find_user_with_username_and_password(read_from_file, lines, users):
    read_from_file.return_value = lines

    user_repository = UserRepository()

    not_matches_conditions = [
        {'username': 'coder', 'password': 'an_not_exists_password'},
        {'username': 'not_exists_usernmae', 'password': 'password'},
        {'username': 'not_exists_usernmae', 'password': 'an_not_exists_password'},

    ]
    for entry in not_matches_conditions:
        username = entry['username']
        password = entry['password']
        user_find = user_repository.find(username, password)

        assert user_find is None
    assert read_from_file.call_count == 4


@mock.patch('user.repository.user_repository.write_to_file')
@mock.patch('user.repository.user_repository.read_from_file')
def test_user_update(read_from_file, write_to_file, lines):
    read_from_file.return_value = lines
    user_repository = UserRepository()

    username = 'coder'
    password = 'coder123'
    user = user_repository.find(username, password)
    user_repository.update(user)
    except_lines = [
        f'{user.username} {user.password} {user.token}'
        for user in user_repository.users
    ]

    assert user in user_repository.users
    write_to_file.assert_called_once_with('/data/users.dat', except_lines)
