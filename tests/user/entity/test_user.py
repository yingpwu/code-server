from user.entity.user import User

    
def test_create_a_user():
    user = User('User', 'User123')

    assert user is not None


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
