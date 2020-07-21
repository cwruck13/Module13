"""
Program: test_gui_guessing_game.py
Author: Cassandra Wruck
Date: 7/21/20

This program tests for the gui_guessing_game.py
"""

import unittest
from topic1 import gui_guessing_game as g
from topic1.gui_guessing_game import generate_random_number


class MyTestCase(unittest.TestCase):

    def setUp(self): #set up
        #guessing number
        self.button_1 = g.pick_one()

    def tearDown(self): #tear down
        del self.button_1

    def test_equal_numbers(self): #made all the attributes
        self.assertEqual(self.button_1, generate_random_number())

if __name__ == '__main__':
    unittest.main()
