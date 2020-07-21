import random as rand
import tkinter




#Reset game
#Else
#Set the button to visible but not clickable
#Add guessed number to guessed_list in object of type NumberGuesser

#functions to let user pick input
#Allow user to push button with their corresponding guess.
def pick_one():
    label.config(text="1")

def pick_two():
    label.config(text="2")

def pick_three():
    label.config(text="3")

def pick_four():
    label.config(text="4")

def pick_five():
    label.config(text="5")

def pick_six():
    label.config(text="6")

def pick_seven():
    label.config(text="7")

def pick_eight():
    label.config(text="8")

def pick_nine():
    label.config(text="9")

def pick_ten():
    label.config(text="10")

#Generates a random number between 1 and MAX.
def generate_random_number():
    global random_number
    random_number = rand.randrange(1,10)
    label.config(str(random_number))

#If correct guess
#Create a WINNER window or messagebox to pop up
#def winner():
  # winner = tkMessageBox.showinfo("WINNER", "User input won")

#Resets games
def clear_func():
    button_1.set("")
    button_2.set("")
    button_3.set("")
    button_4.set("")
    button_5.set("")
    button_6.set("")
    button_7.set("")
    button_8.set("")
    button_9.set("")
    button_10.set("")

g = tkinter.Tk()

''' 
widgets are added here 
'''
#title
g.title('Guessing Game')

#label
label = tkinter.Label(g, text="Waiting for user pick")
label.grid(row=11)


#With buttons each numbered 1 to MAX. You can select 10 or more buttons for this, deciding at design time.
button_1= tkinter.Button(g, text='1', width=10, command=pick_one).grid(row=1)
button_2= tkinter.Button(g, text='2', width=10, command=pick_two).grid(row=2)
button_3= tkinter.Button(g, text='3', width=10, command=pick_three).grid(row=3)
button_4= tkinter.Button(g, text='4', width=10, command=pick_four).grid(row=4)
button_5= tkinter.Button(g, text='5', width=10, command=pick_five).grid(row=5)
button_6= tkinter.Button(g, text='6', width=10, command=pick_six).grid(row=6)
button_7= tkinter.Button(g, text='7', width=10, command=pick_seven).grid(row=7)
button_8= tkinter.Button(g, text='8', width=10, command=pick_eight).grid(row=8)
button_9= tkinter.Button(g, text='9', width=10, command=pick_nine).grid(row=9)
button_10= tkinter.Button(g, text='10', width=10, command=pick_ten).grid(row=10)

#With a button 'Start Game'
button_start = tkinter.Button(g, text='Start Game', width=25).grid(row=12)

button_reset = tkinter.Button(g, text='Reset', width=25, command=clear_func).grid(row=13)

g.mainloop()

class NumberGuesser:
#Write a class NumberGuesser.
#guessed_list - class attribute contains all the guessed numbers, should be empty on new game or reset game
#add_guess - class method that will add to the guessed_list
    pass
