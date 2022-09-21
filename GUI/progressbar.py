from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bar')
root.iconbitmap('C:/Users/dcarson/IdeaProjects/GUI/images/foodicon.ico')
root.geometry('350x200')


def step():
    # my_progress['value'] += 20
    # my_progress.start(10)
    for x in range(10):
        my_label.config(text=my_progress['value'])
        my_progress['value'] += 10
        # slows down task completion?
        root.update_idletasks()
        time.sleep(1)


def stop():
    my_progress.stop()


my_progress = ttk.Progressbar(root, orient=HORIZONTAL,
                              length=310, mode='determinate')
my_button = Button(root, text="Progress", command=step)
my_button2 = Button(root, text="Stop", command=stop)
my_label = Label(root, text="")

my_progress.grid(row=0, column=0, pady=20, padx=20, columnspan=3)
my_button.grid(row=1, column=0, pady=20)
my_button2.grid(row=1, column=2, pady=20, padx=20)
my_label.grid(row=2, column=1)

root.mainloop()