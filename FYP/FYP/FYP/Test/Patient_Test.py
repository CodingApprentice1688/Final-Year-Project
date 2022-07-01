import unittest
from views import views

class testPatient(unittest.TestCase):
    def testLogin():
        assert username == 'wenling'
        assert hashed_password != 'password'
        assert role == 'patient'

if __name__ == '__main__':
   unittest.main()