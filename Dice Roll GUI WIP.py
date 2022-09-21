from tkinter import *
import random

roll_history_list = [] #referred to as the "roll history list"

number_of_dice = 2

number_of_sides = 6

roll_label_exists = False



root = Tk()  # create parent window
root.title("Dice Roller")  # title of the GUI window
root.minsize(900, 600)
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

def remove():
    global roll_label_exists
    if roll_label_exists == False:
        delete_list()
        roll_label_exists = True
        print('if statement worked')
    elif roll_label_exists == True:
        delete_list()
        roll_label
        print('elif statement worked')
    else:
        print('neither statement worked')

def one_diceroll():
    output = random.randint(1,6)
    Label(Roll1_interior, text=output, bg='lightgrey').place(x=123, y=14)
    roll_history_list.append(output)
    remove()

def two_diceroll():
    output1 = random.randint(1,6)
    Label(Roll2_interior, text=output1, bg='lightgrey').place(x=115, y=14)
    output2 = random.randint(1,6)
    Label(Roll2_interior, text=output2, bg='lightgrey').place(x=133, y=14)
    roll_history_list.append(output1)
    roll_history_list.append(output2)
    remove()


Left_frame = Frame(root,  width=200,  height=  400,  bg='grey')
Left_frame.place(x=10, y=10)


Roll1_interior = Frame(Left_frame, width = 170, height = 50, bg='lightgrey')
Roll1_interior.place(x=15, y=10)

roll1 = Button(Roll1_interior, text="Roll 1 Die", command=one_diceroll)
roll1.place(x=30, y=12)


Roll2_interior = Frame(Left_frame, width = 170, height = 50, bg='lightgrey')
Roll2_interior.place(x=15, y=70)

roll2 = Button(Roll2_interior, text="Roll 2 Dice", command=two_diceroll)
roll2.place(x=25, y=12)



Roll_history_frame = Frame(root,  width=880,  height=  100,  bg='grey')
Roll_history_frame.place(x=10, y=425)

Roll_history_interior = Frame(Roll_history_frame,  width=860,  height=80,  bg='lightgrey')
Roll_history_interior.place(x=10, y=10)

roll_label = Label(Roll_history_interior, bg='lightgrey', text=roll_history_list).place(x=100, y=10)

Label(Roll_history_interior, bg='lightgrey', text='Roll History List:').place(x=10, y=10)

def delete_list():
    roll_history_list.clear()
    print('List Cleared')

clearlist_button = Button(Roll_history_interior, text='Clear Roll History', command = lambda : delete_list()) #cannot delete labels after placement becaause there are multiple labels overlapped, python doesn't know which one to delete!
clearlist_button.place(x=10, y=40)


# quit_bar = Frame(left_frame, width = 300, height = 50, bg='lightgrey')
# quit_bar.grid(row=0, column=3, padx=5, pady=5,)
# Button(quit_bar,  text="QUIT",  command=root.quit).grid(padx=5,  pady=5)


# Roll2_interior = Frame(root,  width=430,  height=590,  bg='grey')
# Roll2_interior.grid(row=0,  column=1,  padx=10,  pady=5)


# Label(Roll2_interior).pack(fill='both',  padx=5,  pady=5)
# tool_bar  =  Frame(left_frame,  width=0,  height=0,  bg='lightgrey')
# tool_bar.pack(side='left',  fill='both',  padx=5,  pady=5,  expand=True)

# filter_bar  =  Frame(left_frame,  width=90,  height=185,  bg='lightgrey')
# filter_bar.pack(side='right',  fill='both',  padx=5,  pady=5,  expand=True)


# Button(tool_bar,  text="Crop",  command=clicked).pack(padx=5,  pady=5)
# Button(tool_bar,  text="Rotate &amp; Flip",  command=clicked).pack(padx=5,  pady=5)
# Button(tool_bar,  text="Resize",  command=clicked).pack(padx=5,  pady=5)
# Button(filter_bar,  text="Black &amp; White",  command=clicked).pack(padx=5,  pady=5)



# quit = Button(root, text="QUIT", command=root.quit)
# quit.pack()

# action = Label(root, text="ACTION")
# action.pack()

# def diceroll():
#     output = random.randint(1,6)
#     print("Rolling 1 die...")
#     time.sleep(1)
#     print(output)
#     time.sleep(1)

# def multi_diceroll():
#     print("Rolling 2 dice...")
#     time.sleep(1)
#     for _ in range(2):
#         output = random.randint(1,6)
#         print(output)
#     time.sleep(1)

# def roll_history():
#         print("\nCurrent roll history:")
#         print(roll_history_list)


root.mainloop()

# activebackground & activeforeground -- sets the background or foreground colors when the cursor is over the button
# bd -- sets the border width of button in pixels
# bg & fg -- sets the background and foreground colors
# font -- chooses the text font for the button
# height & width -- sets height and width sizes
# image -- uses an image on the button rather than text

#add and remove history list functionality next