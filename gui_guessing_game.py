import random as rand
import tkinter





#Resets games
#Allow user to push button with their corresponding guess.
#If correct guess
#Create a WINNER window or messagebox to pop up
#Reset game
#Else
#Set the button to visible but not clickable
#Add guessed number to guessed_list in object of type NumberGuesser


g = tkinter.Tk()
''' 
widgets are added here 
'''
#title
g.title('Guessing Game')
g.geometry('400x400')

#With buttons each numbered 1 to MAX. You can select 10 or more buttons for this, deciding at design time.
button_1= tkinter.Button(g, text='1', width=10).pack()
button_2= tkinter.Button(g, text='2', width=10).pack()
button_3= tkinter.Button(g, text='3', width=10).pack()
button_4= tkinter.Button(g, text='4', width=10).pack()
button_5= tkinter.Button(g, text='5', width=10).pack()
button_6= tkinter.Button(g, text='6', width=10).pack()
button_7= tkinter.Button(g, text='7', width=10).pack()
button_8= tkinter.Button(g, text='8', width=10).pack()
button_9= tkinter.Button(g, text='9', width=10).pack()
button_10= tkinter.Button(g, text='10', width=10).pack()

#Generates a random number between 1 and MAX.
def generate_random_number():
    global random_number
    random_number = rand.randrange(1,10)


def pick_one():
    guess = int(button_1.get())

def pick_two():
    guess = int(button_2.get())

#With a button 'Start Game'
button_start = tkinter.Button(g, text='Start Game', width=25).pack()

button_reset = tkinter.Button(g, text='Reset', width=25).pack()

g.mainloop()

class NumberGuesser:
#Write a class NumberGuesser.
#guessed_list - class attribute contains all the guessed numbers, should be empty on new game or reset game
#add_guess - class method that will add to the guessed_list
    pass
