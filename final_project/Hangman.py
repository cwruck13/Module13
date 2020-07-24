"""
Program: Hangman.py
Author: Cassandra Wruck
Date: 7/24/20

This program will have the hangman class that will link to the master class.
"""
#Must used components
#A GUI component
#Multiple functions (or methods)
#Unit testing
#Exception Handling (Try/Except)
#Some sort of user input, including input validation
#Some sort of output
#A class -- used
#You must include nine of the following in your project:
#Decision Structure: If, if-else, if-elif
#Looping Structure: For/while loop
#File I/O
#Inner function
#Function with arbitrary arguments: *args/**kwargs
#Collection: List/tuple
#Collection: Set/dictionary
#Collection: Array
#Case-switch statement
#Datetime
#Python Module or Package
#Data Scraper
#Object Oriented Functionality including constructors/methods/objects
#Object Oriented Program inheritance/polymorphism including base-derived class
#Database connectivity

class Hangman:

    def __int__(self, word):
        self.count=0
        self.gui(word)
