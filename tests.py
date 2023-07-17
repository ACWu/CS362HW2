# OSU CS 362 Summer 2023
# Assignment: HW2
# Student Name: Anthony Wu
# Sutdnet ID: wuant


import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    def test1(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(0))

    def test2(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(1))

    def test3(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(20))

    def test4(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(-1))

    def test5(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(-2))

    def test6(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(19))

    def test7(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(21))

    def test8(self):
        """Verifies if Master Cards with valid lengths and invalid check bits
        returns False
        Picked using White Box Testing - Truth Table"""
        self.assertFalse(contrived_func(10))


if __name__ == '__main__':
    unittest.main(verbosity=2)
