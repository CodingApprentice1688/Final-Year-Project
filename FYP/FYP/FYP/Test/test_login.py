#from entity.User import User
import unittest
from unittest import TestCase

def test_new_user(unittest.TestCase):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User.validateLogin(username, password)
    assert user.username == 'wenling'
    assert user.password == 'password'

