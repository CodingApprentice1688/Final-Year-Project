from entity.User import User

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User.validateLogin(username, password)
    assert user.username == 'wenling'
    assert user.password == 'password'

