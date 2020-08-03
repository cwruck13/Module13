from tkinter import Label, Entry, Canvas, Button
from tkinter.tix import Tk


h = Tk()

#creating gui
h.title("Hangman Game")
h.geometry("500x500")
#h.configure(bg = 'white')

label = Label(h, text = "Enter in your guess:",).place(x = 10, y = 180)
#label1 = Label(h, bg = 'white', text = "The number of letters in the ranodm word is: %s." %(letterNumberStr))
#label1.place(x = 10, y = 120)

input_box = Entry(h)
input_box.place(x = 10, y = 200)


#A canvas is needed so I can draw
canvas = Canvas(h, bg = 'white') # used white background to tell where structure was at
canvas.place(x = 325, y = 200, width = 350, height = 50)

canvas.create_line(10, 400, 100, 400)#scaffoldPart1
canvas.create_line(30, 400, 30, 50)#scaffoldPart2
canvas.create_line(30, 50, 250, 50)#scaffoldPart3
canvas.create_line(175, 50, 175, 100)#rope


h.mainloop()
