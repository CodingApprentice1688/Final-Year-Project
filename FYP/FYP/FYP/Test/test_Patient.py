import unittest
from unittest import TestCase




class test_patient(unittest.TestCase):
    def test_Login(self):
        self.assertTrue(self.username == 'wenling')
        self.assertTrue(self.password == 'password')


if __name__ == '__main__':
    unittest.main()