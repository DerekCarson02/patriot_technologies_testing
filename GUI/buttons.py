from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


myButton = Button(root, text="Ok", command=myClick)

myButton.pack()

root.mainloop()
