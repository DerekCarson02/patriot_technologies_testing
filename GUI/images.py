from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('C:/Users/dcarson/IdeaProjects/GUI/images/foodicon.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/foodicon.ico"))
my_img2 = ImageTk.PhotoImage(Image.open("images/icons8-dell-144.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/icons8-sprite-144.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/icons8-amazon-web-services-144.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/icons8-oracle-logo-144.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


def forward(image_number):
    global my_Label
    global button_forward
    global button_back
    my_Label = Label(image=image_list[image_number])
    my_Label.grid(row=0, column=0, columnspan=3)

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    button_back.grid(row=1, column=0)

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_forward.grid(row=1, column=2)

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=1, column=2)


def back():
    global my_Label
    global button_forward
    global button_back


button_exit = Button(root, text="Exit Program", command=root.quit)
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(1))

my_Label = Label(image=image_list[0])

my_Label.grid(row=0, column=0, columnspan=3)

button_forward.grid(row=1, column=2)
button_exit.grid(row=1, column=1)
button_back.grid(row=1, column=0)

root.mainloop()

# Incomplete program
