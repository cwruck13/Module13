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

from tkinter import *
import random
from tkinter import messagebox
import collections
from structure import *

#Initializing Empty List

mywords=[]

#importing word list
word_file = open("randomwords.txt","r")

#Appending words from file to the list
for x in word_file:
    mywords.append(x.replace('\n', ''))

word=random.choice(mywords)
random_word=list(word)
w=[]
s='_ '*len(random_word)
w=s.split(' ')
w.pop(len(random_word))
actual=random_word.copy()

#12 characters in the longest word
word_letters = ["char_1", "char_2", "char_3", "char_4", "char_5", "char_6", "char_7", "char_8", "char_9", "char_10", "char_11", "char_12", "char_13"]

position_x = 10
user_life = 6
label_x = 10
entry = {} #dictionary

def logic():
    global letter_number
    global user_life
    global label_x
    user_input = input_box.get()

    if not user_input: #not will test if string is empty
        messagebox.showinfo("Input", "No letter entered")

    else:
        if user_input in word: #if word is in the word list

            letter_position = random_word.index(user_input)
            #if - elis to determine letters in the word based on a list form
            if letter_position == 0:

                entry['char_1'].configure(state = ('normal'))
                entry['char_1'].insert(0, user_input)
                entry['char_1' + str(1)].configure(state = ('readonly'))
                random_word[0] = ""
                letter_number -= 1

            elif letter_position == 1:

                entry['char_2'].configure(state = ('normal'))
                entry['char_2'].insert(0, user_input)
                entry['char_2'].configure(state = ('readonly'))
                random_word[1] = ""
                letter_number -= 1

            elif letter_position == 2:
                entry['char_3'].configure(state = ('normal'))
                entry['char_3'].insert(0, user_input)
                entry['char_3'].configure(state = ('readonly'))
                random_word[2] = ""
                letter_number -= 1

            elif letter_position ==3:
                entry['char_4'].configure(state = ('normal'))
                entry['char_4'].insert(0, user_input)
                entry['char_4'].configure(state = ('readonly'))
                random_word[3] = ""
                letter_number -= 1

            elif letter_position == 4:
                entry['char_5'].configure(state = ('normal'))
                entry['char_5'].insert(0, user_input)
                entry['char_5' + str(1)].configure(state = ('readonly'))
                random_word[4] = ""
                letter_number -= 1

            elif letter_position == 5:
                entry['char_6'].configure(state = ('normal'))
                entry['char_6'].insert(0, user_input)
                entry['char_6'].configure(state = ('readonly'))
                random_word[5] = ""
                letter_number -= 1

            elif letter_position == 6:
                entry['char_7'].configure(state = ('normal'))
                entry['char_7'].insert(0, user_input)
                entry['char_7'].configure(state = ('readonly'))
                random_word[6] = ""
                letter_number -= 1

            elif letter_position == 7:
                entry['char_8'].configure(state = ('normal'))
                entry['char_8'].insert(0, user_input)
                entry['char_8'].configure(state = ('readonly'))
                random_word[7] = ""
                letter_number -= 1

            elif letter_position ==8:
                entry['char_9'].configure(state = ('normal'))
                entry['char_9'].insert(0, user_input)
                entry['char_9'].configure(state = ('readonly'))
                random_word[8] = ""
                letter_number -= 1

            elif letter_position == 9:
                entry['char_10'].configure(state = ('normal'))
                entry['char_10'].insert(0, user_input)
                entry['char_10'].configure(state = ('readonly'))
                random_word[9] = ""
                letter_number -= 1

            elif letter_position == 10:
                entry['char_11'].configure(state = ('normal'))
                entry['char_11'].insert(0, user_input)
                entry['char_11'].configure(state = ('readonly'))
                random_word[10] = ""
                letter_number -= 1

            elif letter_position == 11:
                entry['char_12'].configure(state = ('normal'))
                entry['char_12'].insert(0, user_input)
                entry['char_12'].configure(state = ('readonly'))
                random_word[11] = ""
                letter_number -= 1

            elif letter_position == 12:
                entry['char_13'].configure(state = ('normal'))
                entry['char_13'].insert(0, user_input)
                entry['char_13'].configure(state = ('readonly'))
                random_word[12] = ""
                letter_number -= 1

            if letter_number == 0:
                messagebox.showinfo("Won", "You correctly guessed the secret word: %s." %(random_word))


        else:
            #takes away a life every time a wrong letter is entered
            user_life -= 1
            if label_x == (10 + 50)+ (50*5):
                return
            else:
                letters_entered = Label(h, text = user_input).place(x = label_x , y = 500) #displays the wrong letter
            label_x += 50
            #as users lifes go down, man is drawn
            if user_life == 5:
                canvas.create_oval(150, 100, 200, 150)#head

            if user_life == 4:
                canvas.create_line(175, 150, 175, 225)#chest

            if user_life == 3:
                canvas.create_line(175, 150, 150, 200)#leftArm

            if user_life == 2:
                canvas.create_line(175, 150, 200, 200)#rightArm

            if user_life == 1:
                canvas.create_line(175, 225, 150, 300)#leftLeg

            if user_life == 0:
                canvas.create_line(175, 225, 200, 300)#rightLeg
                messagebox.showinfo("Lost", "You have run out of lives the random word was: %s." %(random_word))

            #while loop to take out unnecessary items
        while letter_number != len(word_letters):
            word_letters.pop(-1)

submit_button = Button(h, text = "Submit letter",command = logic).place(x = 200, y = 195) #wasn't sure how to place button because can't have both programs using each other




