from tkinter import *
import random

number_list = [] 

x=6

#--------------------------------------------------------------------------------------------------------
#root window
root = Tk()  # create parent window
root.title("Dice Roller")  # title of the GUI window
root.minsize(900, 700)
root.maxsize(900, 700)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color


#--------------------------------------------------------------------------------------------------------
#functions for rolling dice
def one_diceroll():
    output = random.randint(1,x)
    Label(Roll1_interior, text=str(output)+' ', bg='white').place(x=123, y=14)
    number_list.append(output)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)

def two_diceroll():
    output1 = random.randint(1,x)
    Label(Roll2_interior, text=str(output1)+' ', bg='white').place(x=109, y=14) #left
    output2 = random.randint(1,x)
    Label(Roll2_interior, text=str(output2)+' ', bg='white').place(x=139, y=14) #right
    number_list.append(output1)
    number_list.append(output2)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)

def three_diceroll():
    output1 = random.randint(1,x)
    Label(Roll3_interior, text=str(output1)+' ', bg='white').place(x=87, y=14) #left
    output2 = random.randint(1,x)
    Label(Roll3_interior, text=str(output2)+' ', bg='white').place(x=117, y=14) #center
    output3 = random.randint(1,x)
    Label(Roll3_interior, text=str(output3)+' ', bg='white').place(x=147, y=14) #right
    number_list.append(output1)
    number_list.append(output2)
    number_list.append(output3)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)

def four_diceroll():
    output1 = random.randint(1,x)
    Label(Roll4_interior, text=str(output1)+' ', bg='white').place(x=109, y=14) #top left
    output2 = random.randint(1,x)
    Label(Roll4_interior, text=str(output2)+' ', bg='white').place(x=139, y=14) #top right
    output3 = random.randint(1,x)
    Label(Roll4_interior, text=str(output3)+' ', bg='white').place(x=109, y=43) #bottom left
    output4 = random.randint(1,x)
    Label(Roll4_interior, text=str(output4)+' ', bg='white').place(x=139, y=43) #bottom right
    number_list.append(output1)
    number_list.append(output2)
    number_list.append(output3)
    number_list.append(output4)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)

def five_diceroll():
    output1 = random.randint(1,x)
    Label(Roll5_interior, text=str(output1)+' ', bg='white').place(x=94, y=14) #top left
    output2 = random.randint(1,x)
    Label(Roll5_interior, text=str(output2)+' ', bg='white').place(x=140, y=14) #top right
    output3 = random.randint(1,x)
    Label(Roll5_interior, text=str(output3)+' ', bg='white').place(x=117, y=36) #center
    output4 = random.randint(1,x)
    Label(Roll5_interior, text=str(output4)+' ', bg='white').place(x=94, y=58) #bottom left
    output5 = random.randint(1,x)
    Label(Roll5_interior, text=str(output5)+' ', bg='white').place(x=140, y=58) #bottom right
    number_list.append(output1) 
    number_list.append(output2) 
    number_list.append(output3) 
    number_list.append(output4) 
    number_list.append(output5)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)

def six_diceroll():
    output1 = random.randint(1,x)
    Label(Roll6_interior, text=str(output1)+' ', bg='white').place(x=94, y=24) #top left
    output2 = random.randint(1,x)
    Label(Roll6_interior, text=str(output2)+' ', bg='white').place(x=117, y=24) #top center
    output3 = random.randint(1,x)
    Label(Roll6_interior, text=str(output3)+' ', bg='white').place(x=140, y=24) #top right
    output4 = random.randint(1,x)
    Label(Roll6_interior, text=str(output4)+' ', bg='white').place(x=94, y=48) #bottom left
    output5 = random.randint(1,x)
    Label(Roll6_interior, text=str(output5)+' ', bg='white').place(x=117, y=48) #bottom center
    output6 = random.randint(1,x)
    Label(Roll6_interior, text=str(output6)+' ', bg='white').place(x=140, y=48) #bottom right
    number_list.append(output1)
    number_list.append(output2)
    number_list.append(output3)
    number_list.append(output4)
    number_list.append(output5)
    number_list.append(output6)
    Label(Roll_history_interior, bg='lightgrey', text=number_list).place(x=100, y=10)


#--------------------------------------------------------------------------------------------------------
#functions for "clearing" the squares by placing blank labels over them
def clear_roll1():
    Label(Roll1_interior, text="  ", bg='white').place(x=126, y=14)


def clear_roll2():
    Label(Roll2_interior, text="  ", bg='white').place(x=112, y=14) #left
    Label(Roll2_interior, text="  ", bg='white').place(x=142, y=14) #right


def clear_roll3():
    Label(Roll3_interior, text="  ", bg='white').place(x=90, y=14) #left
    Label(Roll3_interior, text="  ", bg='white').place(x=120, y=14) #middle
    Label(Roll3_interior, text="  ", bg='white').place(x=150, y=14) #right


def clear_roll4():
    Label(Roll4_interior, text="  ", bg='white').place(x=112, y=14) #top left
    Label(Roll4_interior, text="  ", bg='white').place(x=142, y=14) #top right

    Label(Roll4_interior, text="  ", bg='white').place(x=112, y=43) #bottom left
    Label(Roll4_interior, text="  ", bg='white').place(x=142, y=43) #bottom right


def clear_roll5():
    Label(Roll5_interior, text="  ", bg='white').place(x=97, y=14) #top left
    Label(Roll5_interior, text="  ", bg='white').place(x=143, y=14) #top right

    Label(Roll5_interior, text="  ", bg='white').place(x=120, y=36) #center

    Label(Roll5_interior, text="  ", bg='white').place(x=97, y=58) #bottom left
    Label(Roll5_interior, text="  ", bg='white').place(x=143, y=58) #bottom right


def clear_roll6():
    Label(Roll6_interior, text="  ", bg='white').place(x=97, y=24) #top left
    Label(Roll6_interior, text="  ", bg='white').place(x=120, y=24) #top middle
    Label(Roll6_interior, text="  ", bg='white').place(x=143, y=24) #top right

    Label(Roll6_interior, text="  ", bg='white').place(x=97, y=48) #bottom left
    Label(Roll6_interior, text="  ", bg='white').place(x=120, y=48) #bottom middle
    Label(Roll6_interior, text="  ", bg='white').place(x=143, y=48) #bottom right


def clear_all():
    clear_roll1()
    clear_roll2()
    clear_roll3()
    clear_roll4()
    clear_roll5()
    clear_roll6()


#--------------------------------------------------------------------------------------------------------
#frame for rolling dice 
frame = Frame(root,  width=222,  height=513, bg='grey')
frame.place(x=10, y=65)

frame_header = Frame(root, width=222, height=50, bg='grey')
frame_header.place(x=10, y=20)

header_frame = Frame(frame_header, width=175, height=20, bg='lightgrey')
header_frame.place(x=23, y=15)
current_roll_status = Label(header_frame, text=f'Currently Rolling {x}-Sided Dice...', bg='lightgrey')
current_roll_status.place(x=0, y=0)

#roll 1 die
Roll1_interior = Frame(frame, width=170, height=50, bg='lightgrey')
Roll1_interior.place(x=40, y=10)
Button(Roll1_interior, text="Roll 1 Die", command=one_diceroll).place(x=10, y=12)
Frame(Roll1_interior, width=20, height=21, bg='white').place(x=119, y=14)
#clear button
Button(frame, text="X", fg='red', command=clear_roll1).place(x=12, y=22)


#roll 2 dice
Roll2_interior = Frame(frame, width=170, height=50, bg='lightgrey')
Roll2_interior.place(x=40, y=70)
Button(Roll2_interior, text="Roll 2 Dice", command=two_diceroll).place(x=10, y=12)
Frame(Roll2_interior, width=20, height=21, bg='white').place(x=105, y=14)
Frame(Roll2_interior, width=20, height=21, bg='white').place(x=135, y=14)
#clear button
Button(frame, text="X", fg='red', command=clear_roll2).place(x=12, y=82)


#roll 3 dice
Roll3_interior = Frame(frame, width=170, height=50, bg='lightgrey')
Roll3_interior.place(x=40, y=130)
Button(Roll3_interior, text="Roll 3 Dice", command=three_diceroll).place(x=10, y=12)
Frame(Roll3_interior, width=20, height=21, bg='white').place(x=83, y=14)
Frame(Roll3_interior, width=20, height=21, bg='white').place(x=113, y=14)
Frame(Roll3_interior, width=20, height=21, bg='white').place(x=143, y=14)
#clear button
Button(frame, text="X", fg='red', command=clear_roll3).place(x=12, y=142)


#roll 4 dice
Roll4_interior = Frame(frame, width=170, height=80, bg='lightgrey')
Roll4_interior.place(x=40, y=190)
Button(Roll4_interior, text="Roll 4 Dice", command=four_diceroll).place(x=10, y=26)
Frame(Roll4_interior, width=20, height=21, bg='white').place(x=105, y=14)
Frame(Roll4_interior, width=20, height=21, bg='white').place(x=135, y=14)
Frame(Roll4_interior, width=20, height=21, bg='white').place(x=105, y=43)
Frame(Roll4_interior, width=20, height=21, bg='white').place(x=135, y=43)
#clear button
Button(frame, text="X", fg='red', command=clear_roll4).place(x=12, y=216)


#roll 5 dice
Roll5_interior = Frame(frame, width=170, height=95, bg='lightgrey')
Roll5_interior.place(x=40, y=280)
Button(Roll5_interior, text="Roll 5 Dice", command=five_diceroll).place(x=10, y=32)
Frame(Roll5_interior, width=20, height=21, bg='white').place(x=90, y=14)
Frame(Roll5_interior, width=20, height=21, bg='white').place(x=113, y=36)
Frame(Roll5_interior, width=20, height=21, bg='white').place(x=136, y=14)
Frame(Roll5_interior, width=20, height=21, bg='white').place(x=90, y=58)
Frame(Roll5_interior, width=20, height=21, bg='white').place(x=136, y=58)
#clear button
Button(frame, text="X", fg='red', command=clear_roll5).place(x=12, y=313)


#roll 6 dice
Roll6_interior = Frame(frame, width=170, height=95, bg='lightgrey')
Roll6_interior.place(x=40, y=385)
Button(Roll6_interior, text="Roll 6 Dice", command=six_diceroll).place(x=10, y=32)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=90, y=24)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=113, y=24)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=136, y=24)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=90, y=48)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=113, y=48)
Frame(Roll6_interior, width=20, height=21, bg='white').place(x=136, y=48)\
#clear button
Button(frame, text="X", fg='red', command=clear_roll6).place(x=12, y=418)


#clear all button
Button(frame, text="Clear All", fg='red', command=clear_all).place(x=95, y=484)

#--------------------------------------------------------------------------------------------------------
#functions that change the die size
def change_size2():
    global x
    x = 2
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice... ', bg='lightgrey').place(x=0, y=0)

def change_size4():
    global x
    x = 4
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice... ', bg='lightgrey').place(x=0, y=0)

def change_size6():
    global x
    x = 6
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice... ', bg='lightgrey').place(x=0, y=0)

def change_size8():
    global x
    x = 8
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice... ', bg='lightgrey').place(x=0, y=0)

def change_size10():
    global x
    x = 10
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice...', bg='lightgrey').place(x=0, y=0)

def change_size12():
    global x
    x = 12
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice...', bg='lightgrey').place(x=0, y=0)

def change_size20():
    global x
    x = 20
    Label(header_frame, text=f'Currently Rolling {x}-Sided Dice...', bg='lightgrey').place(x=0, y=0)


#--------------------------------------------------------------------------------------------------------
#frame for choosing dice size/game info
frame2 = Frame(root,  width=645,  height=558, bg='grey')
frame2.place(x=245, y=20)

frame2_selection = Frame(frame2, width=621, height=302, bg='lightgrey')
frame2_selection.place(x=12, y=12)

frame2_selection_header = Frame(frame2_selection, width=200, height=35, bg='grey')
frame2_selection_header.place(x=200, y=0)
Label(frame2_selection_header, text="Select What Size Dice to Roll", bg='lightgrey').place(x=23, y=0)

Button(frame2_selection, text="2-Sided Dice", command=change_size2).place(x=100, y=50)
Button(frame2_selection, text="4-Sided Dice", command=change_size4).place(x=207, y=50)
Button(frame2_selection, text="6-Sided Dice", command=change_size6).place(x=320, y=50)
Button(frame2_selection, text="8-Sided Dice", command=change_size8).place(x=430, y=50)

Button(frame2_selection, text="10-Sided Dice", command=change_size10).place(x=150, y=185)
Button(frame2_selection, text="12-Sided Dice", command=change_size12).place(x=265, y=185)
Button(frame2_selection, text="20-Sided Dice", command=change_size20).place(x=380, y=185)

frame2_info = Frame(frame2, width=621, height=221, bg='lightgrey')
frame2_info.place(x=12, y=325)
frame2_info_interior = Frame(frame2_info, width=570, height=177, bg='white').place(x=25, y=22)

Label(frame2_info_interior, text="Dice Roller", bg='white').place(x=525, y=410)
Label(frame2_info_interior, text="v2.2.0", bg='white').place(x=536, y=435)
Label(frame2_info_interior, text="Created By Zachery George", bg='white').place(x=485, y=460)
Label(frame2_info_interior, text="2022", bg='white').place(x=540, y=485)

#--------------------------------------------------------------------------------------------------------
#frame for roll history at bottom of screen
Roll_history_frame = Frame(root,  width=880,  height=100,  bg='grey')
Roll_history_frame.place(x=10, y=590)


Roll_history_interior = Frame(Roll_history_frame,  width=859,  height=80,  bg='lightgrey')
Roll_history_interior.place(x=11, y=10)
Label(Roll_history_interior, bg='lightgrey', text='Roll History List:').place(x=10, y=10)


def clear_list():
    number_list.clear()
    Label(Roll_history_interior, bg='lightgrey', text='                                                                                                                                                                                                                                                                                                                                 ').place(x=100, y=10)

clearlist_button = Button(Roll_history_interior, text='Clear Roll History', command = lambda : clear_list()) 
clearlist_button.place(x=10, y=40)


#--------------------------------------------------------------------------------------------------------
#unused/unfishied functionality:

# def sum_list():
#     print(sum(number_list))
    
# list_sum_button = Button(Roll_history_interior, text='Sum of Rolls:', command=sum_list)
# list_sum_button.place(x=120, y=40)

#list can hold ~84 digits before running out of space, implement feature that clears list after exceeding 84 characters:
# def no_space():
#     if number_list[84] == True:
#         clear_list()
#     else:
#         print("Not at 84")
#--------------------------------------------------------------------------------------------------------


root.mainloop()

# activebackground & activeforeground -- sets the background or foreground colors when the cursor is over the button
# bd -- sets the border width of button in pixels
# bg & fg -- sets the background and foreground colors
# font -- chooses the text font for the button
# height & width -- sets height and width sizes
# image -- uses an image on the button rather than text
