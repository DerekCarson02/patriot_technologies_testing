import random
import time

roll_history_list = ["This list is empty because you haven't rolled yet!"] #referred to as the "roll history list"

number_of_sides = 6 #sets default die to 6-sided

number_of_dice = 0 #placeholder value for the number of dice to roll before user chooses and it is assigned a value

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# this function is the initial dice roll prompt, and is only ran once the very first time. After that following_dicerolls() always takes its place.
def initial_diceroll():
    ask = input(f"Would you like to roll the {number_of_sides}-sided die? [Yes] [No]\n")
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'yup' or ask == 'YES' or ask == 'Yes ' or ask == 'yes ' or ask == 'y ' or ask == 'yup ' or ask == 'YES ':
        roll_history_list.remove("This list is empty because you haven't rolled yet!") #this line removes the "empty" message in the roll history list, this feature makes the initial_diceroll() function necessary and separate from following_dicerolls()
        diceroll()
        return roll_again()
    elif ask == 'No' or ask == 'no' or ask == 'n' or ask == 'nope' or ask== 'NO' or ask == 'No ' or ask == 'no ' or ask == 'n ' or ask == 'nope ' or ask== 'NO ':
        quit_text()
        time.sleep(1)
        return "Done."
    elif ask == 'history' or ask == 'History' or ask == 'hi' or ask == 'HISTORY' or  ask == 'history ' or ask == 'History ' or ask == 'hi ' or ask == 'HISTORY ':
        print("\nCurrent roll history:")
        print(roll_history_list)
        print("")
        return initial_diceroll()
    elif ask == 'change' or ask == 'Change' or ask == 'c' or ask == 'CHANGE' or ask == 'change ' or ask == 'Change ' or ask == 'c ' or ask == 'CHANGE ':
        print("")
        change_die_size()
        print("")
        return initial_diceroll()
    elif ask == 'help' or ask == 'Help' or ask == 'he' or ask == 'HELP' or ask == 'help ' or ask == 'Help ' or ask == 'he ' or ask == 'HELP ':
        print(startup_menu())
        return initial_diceroll()
    elif ask == 'about' or ask == 'About' or ask == 'a' or ask == 'ABOUT' or ask == 'about ' or ask == 'About ' or ask == 'a ' or ask == 'ABOUT ':
        print(about())
        return initial_diceroll()
    elif ask == 'more' or ask == 'More' or ask == 'm' or ask == 'MORE' or ask == 'more ' or ask == 'More ' or ask == 'm ' or ask == 'MORE ':
        initial_determine_number_of_dice()
        print(f"Okay, you are now rolling {number_of_dice} dice.")
        roll_history_list.remove("This list is empty because you haven't rolled yet!")
        multi_diceroll()
        return roll_again()
    else:
        confused_prompt()
        return initial_diceroll()


#this function acts the same as initial_diceroll(), but it does not remove the "empty" message from the roll history list since it was already removed during the first initial roll
def following_dicerolls():
    ask = input(f"Would you like to roll the {number_of_sides}-sided die? [Yes] [No]\n")
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'yup' or ask == 'YES' or ask == 'Yes ' or ask == 'yes ' or ask == 'y ' or ask == 'yup ' or ask == 'YES ':
        diceroll()
        return roll_again()
    elif ask == 'No' or ask == 'no' or ask == 'n' or ask == 'nope' or ask== 'NO' or ask == 'No ' or ask == 'no ' or ask == 'n ' or ask == 'nope ' or ask== 'NO ':
        quit_text()
        time.sleep(1)
        return "Done."
    elif ask == 'history' or ask == 'History' or ask == 'hi' or ask == 'HISTORY' or  ask == 'history ' or ask == 'History ' or ask == 'hi ' or ask == 'HISTORY ':
        print("\nCurrent roll history:")
        print(roll_history_list)
        print("")
        return following_dicerolls()
    elif ask == 'change' or ask == 'Change' or ask == 'c' or ask == 'CHANGE' or ask == 'change ' or ask == 'Change ' or ask == 'c ' or ask == 'CHANGE ':
        print("")
        change_die_size()
        print("")
        return following_dicerolls()
    elif ask == 'help' or ask == 'Help' or ask == 'he' or ask == 'HELP' or ask == 'help ' or ask == 'Help ' or ask == 'he ' or ask == 'HELP ':
        print(startup_menu())
        return following_dicerolls()
    elif ask == 'about' or ask == 'About' or ask == 'a' or ask == 'ABOUT' or ask == 'about ' or ask == 'About ' or ask == 'a ' or ask == 'ABOUT ':
        print(about())
        return following_dicerolls()
    elif ask == 'more' or ask == 'More' or ask == 'm' or ask == 'MORE' or ask == 'more ' or ask == 'More ' or ask == 'm ' or ask == 'MORE ':
        following_determine_number_of_dice()
        print(f"Okay, you are now rolling {number_of_dice} dice.")
        multi_diceroll()
        return roll_again()
    else:
        confused_prompt()
        return following_dicerolls()


#this function is for every dice roll prompt after the first one    
def roll_again():
    ask = input(f"Would you like to roll the {number_of_sides}-sided again? [Yes] [No]\n")
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'yup' or ask == 'YES' or ask == 'Yes ' or ask == 'yes ' or ask == 'y ' or ask == 'yup ' or ask == 'YES ':
        diceroll()
        return roll_again()
    elif ask == 'No' or ask == 'no' or ask == 'n' or ask == 'nope' or ask == 'NO' or ask == 'No ' or ask == 'no ' or ask == 'n ' or ask == 'nope ' or ask == 'NO ':
        quit_text()
        time.sleep(1)
        return "Done."
    elif ask == 'history' or ask == 'History' or ask == 'hi' or ask == 'HISTORY' or ask == 'history ' or ask == 'History ' or ask == 'hi ' or ask == 'HISTORY ':
        print("\nCurrent roll history:")
        print(roll_history_list)
        print("")
        return roll_again()
    elif ask == 'change' or ask == 'Change' or ask == 'c' or ask == 'CHANGE' or ask == 'change ' or ask == 'Change ' or ask == 'c ' or ask == 'CHANGE ':
        print("")
        change_die_size()
        print("")
        return following_dicerolls()
    elif ask == 'help' or ask == 'Help' or ask == 'he' or ask == 'HELP' or ask == 'help ' or ask == 'Help ' or ask == 'he ' or ask == 'HELP ':
        print(startup_menu())
        return following_dicerolls()
    elif ask == 'about' or ask == 'About' or ask == 'a' or ask == 'ABOUT' or ask == 'about ' or ask == 'About ' or ask == 'a ' or ask == 'ABOUT ':
        print(about())
        return following_dicerolls()
    elif ask == 'more' or ask == 'More' or ask == 'm' or ask == 'MORE' or ask == 'more ' or ask == 'More ' or ask == 'm ' or ask == 'MORE ':
        roll_again_determine_number_of_dice()
        print(f"Okay, you are now rolling {number_of_dice} dice.")
        multi_diceroll()
        return roll_again()
    else:
        confused_prompt()
        return roll_again()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#the action of rolling more than one die
def multi_diceroll():
    print("")
    multi_rolling_text()
    print("")
    time.sleep(1)
    for _ in range(number_of_dice):
        output = random.randint(1,number_of_sides)
        print(output)
        roll_history_list.append(output) #adds output of range to the roll history list
    print("")
    time.sleep(1)

#the action of rolling the die + adding on to the roll history list
def diceroll():
    output = random.randint(1,number_of_sides)
    print("")
    rolling_text()
    print("")
    time.sleep(1)
    print(output)
    roll_history_list.append(output)
    print("")
    time.sleep(1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#functions for the printed repsonses to user input
def confused_prompt(): #called when input doesn't make sense
    print("\nHuh? I don't understand what that means. Please try again!\n")

def quit_text(): #called when player chooses not to roll the die
    print("\nOkay! Quiting...")

def rolling_text(): #called in diceroll() when player chooses to roll the die
    print(f"Rolling {number_of_sides}-sided die...")

def multi_rolling_text(): #called in multi_diceroll() when player chooses to roll multiple dice
    print(f"Rolling {number_of_dice} {number_of_sides}-sided dice...")

def startup_menu():
    return "Type 'About' anytime to learn about the program.\nType 'Help' anytime to show this menu again.\n\nType 'History' anytime to view the current roll history.\nType 'Change' anytime to change the size of the die. The default is a 6-sided die.\nType 'More' anytime to roll more than one die at once.\n----------------------------------------------------------------------------------------------"

def about():
    return "\n\n\nDice Roller\nCreated by Zachery George\nv1.4.0\n----------------------------------------------------------------------------------------------"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#function that changes the die size
def change_die_size():
    die_size = input("What type of die do you want to roll? [2] [4] [6] [8] [10] [12] [20]\n")
    global number_of_sides
    if die_size == '2':
        number_of_sides = 2
    elif die_size == '4':
        number_of_sides = 4
    elif die_size == '6':
        number_of_sides = 6
    elif die_size == '8':
        number_of_sides = 8
    elif die_size == '10':
        number_of_sides = 10
    elif die_size == '12':
        number_of_sides = 12
    elif die_size == '20':
        number_of_sides = 20
    else:
        confused_prompt()
        return change_die_size()


#function that change the number of dice rolled
def initial_determine_number_of_dice():
    ask = input(f"\nHow many {number_of_sides}-sided dice would you like to roll at once? [2] [3] [4] [5] [6] [7] [Cancel]\n")
    global number_of_dice
    if ask == "2" or ask == '2 ' or ask == 'two' or ask == 'TWO' or ask == 'two ' or ask == 'TWO ':
        number_of_dice = 2
    elif ask == "3" or ask == '3 ' or ask == 'three' or ask == 'THREE' or ask == 'three ' or ask == 'THREE ':
        number_of_dice = 3
    elif ask == "4" or ask == '4 ' or ask == 'four' or ask == 'FOUR' or ask == 'four ' or ask == 'FOUR ':
        number_of_dice = 4
    elif ask == "5" or ask == '5 ' or ask == 'five' or ask == 'FIVE' or ask == 'five ' or ask == 'FIVE ':
        number_of_dice = 5
    elif ask == "6" or ask == '6 ' or ask == 'six' or ask == 'SIX' or ask == 'six ' or ask == 'SIX ':
        number_of_dice = 6
    elif ask == "7" or ask == '7 ' or ask == 'seven' or ask == 'SEVEN' or ask == 'seven ' or ask == 'SEVEN ':
        number_of_dice = 7
    elif ask == 'Cancel' or ask == 'cancel' or ask == 'CANCEL' or ask == 'c' or ask == 'Cancel ' or ask == 'cancel ' or ask == 'CANCEL ' or ask == 'c ':
        print("Canceled. Returning...")
        return initial_diceroll()
    else:
        confused_prompt()
        return initial_determine_number_of_dice()


def following_determine_number_of_dice():
    ask = input(f"\nHow many {number_of_sides}-sided dice would you like to roll at once? [2] [3] [4] [5] [6] [7] [Cancel]\n")
    global number_of_dice
    if ask == "2" or ask == '2 ' or ask == 'two' or ask == 'TWO' or ask == 'two ' or ask == 'TWO ':
        number_of_dice = 2
    elif ask == "3" or ask == '3 ' or ask == 'three' or ask == 'THREE' or ask == 'three ' or ask == 'THREE ':
        number_of_dice = 3
    elif ask == "4" or ask == '4 ' or ask == 'four' or ask == 'FOUR' or ask == 'four ' or ask == 'FOUR ':
        number_of_dice = 4
    elif ask == "5" or ask == '5 ' or ask == 'five' or ask == 'FIVE' or ask == 'five ' or ask == 'FIVE ':
        number_of_dice = 5
    elif ask == "6" or ask == '6 ' or ask == 'six' or ask == 'SIX' or ask == 'six ' or ask == 'SIX ':
        number_of_dice = 6
    elif ask == "7" or ask == '7 ' or ask == 'seven' or ask == 'SEVEN' or ask == 'seven ' or ask == 'SEVEN ':
        number_of_dice = 7
    elif ask == 'Cancel' or ask == 'cancel' or ask == 'CANCEL' or ask == 'c' or ask == 'Cancel ' or ask == 'cancel ' or ask == 'CANCEL ' or ask == 'c ':
        print("Canceled. Returning...")
        return following_dicerolls()
    else:
        confused_prompt()
        return following_determine_number_of_dice()


def roll_again_determine_number_of_dice():
    ask = input(f"\nHow many {number_of_sides}-sided dice would you like to roll at once? [2] [3] [4] [5] [6] [7] [Cancel]\n")
    global number_of_dice
    if ask == "2" or ask == '2 ' or ask == 'two' or ask == 'TWO' or ask == 'two ' or ask == 'TWO ':
        number_of_dice = 2
    elif ask == "3" or ask == '3 ' or ask == 'three' or ask == 'THREE' or ask == 'three ' or ask == 'THREE ':
        number_of_dice = 3
    elif ask == "4" or ask == '4 ' or ask == 'four' or ask == 'FOUR' or ask == 'four ' or ask == 'FOUR ':
        number_of_dice = 4
    elif ask == "5" or ask == '5 ' or ask == 'five' or ask == 'FIVE' or ask == 'five ' or ask == 'FIVE ':
        number_of_dice = 5
    elif ask == "6" or ask == '6 ' or ask == 'six' or ask == 'SIX' or ask == 'six ' or ask == 'SIX ':
        number_of_dice = 6 
    elif ask == "7" or ask == '7 ' or ask == 'seven' or ask == 'SEVEN' or ask == 'seven ' or ask == 'SEVEN ':
        number_of_dice = 7
    elif ask == 'Cancel' or ask == 'cancel' or ask == 'CANCEL' or ask == 'c' or ask == 'Cancel ' or ask == 'cancel ' or ask == 'CANCEL ' or ask == 'c ':
        return roll_again()
    else:
        confused_prompt()
        return roll_again_determine_number_of_dice()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#introduction text
print(about())
print(startup_menu())


#runs program
print(initial_diceroll())
