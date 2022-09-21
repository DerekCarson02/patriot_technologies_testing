from openpyxl import Workbook
import sys
import os.path

customer = "Extreme Networks"
wDPath = r'C:/Users/dcarson/Documents/Excel Test/'


def file_exists(response):
    fileCheck = os.path.exists(wDPath + "WO00000" + response + ".xlsx")
    if fileCheck:
        print("{} already exists in this folder! DO NOT overwrite existing work orders!".format("WO00000" + response))
        return False
    return True


def validResponse(character_limit, character_type_alnum, response):
    if character_type_alnum:
        if response.isnumeric():
            print("This field does not accept numbers!")
            return False
        elif len(response) == 0:
            print("Please enter something into the prompt.")
            return False
        elif len(response) > int(character_limit):
            print("This field has a character limit of {}!".format(character_limit))
            return False
        elif len(response) < int(character_limit):
            print("At least {} characters should be used for this field!".format(character_limit))
            return False

    if not character_type_alnum:
        if response.isalpha():
            print("This field does not accept letters!")
            return False
        elif len(response) == 0:
            print("Please enter something into the prompt.")
            return False
        elif len(response) > int(character_limit):
            print("This field has a character limit of {}!".format(character_limit))
            return False
        elif len(response) < int(character_limit):
            print("At least {} characters should be used for this field!".format(character_limit))
            return False

    return True


def yes_or_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        space()
        print("Please enter (y/n)")
        print(question + ' (y/n): ')
        return False


def space():
    print("")


def createWorkBook(workOrder, model):
    wbfilename = "WO00000" + workOrder
    destination_filename_path = '{}{}.xlsx'.format(wDPath, wbfilename)

    # Creating workbook object.
    wb = Workbook()

    # Creating worksheet.
    ws1 = wb.active
    ws1.title = workOrder
    ws1['A1'] = wbfilename
    ws1['C1'] = model

    wb.save(filename=destination_filename_path)
    return destination_filename_path


modelList = ['FGEXT4120C', 'FGEXTE3120', 'FGEXTE3122', 'FGEXTE2122', 'E1120']

workOrderName = input("Please enter your work order number: ")
space()

while not (validResponse(3, False, workOrderName) and file_exists(workOrderName)):
    workOrderName = input("Please enter your work order number: ")
    space()

for x in range(len(modelList)):
    print("{}.)  '{}'".format(x, modelList[x]))
space()
modelSelect = input("Please select the index according to your model name: [0|{}]  ".format(len(modelList) - 1))
space()

while True:
    # Checking for out of index errors
    try:
        while not (validResponse(1, False, modelSelect)
                   and yes_or_no("Is {} the correct selection?".format(modelList[int(modelSelect)]))):
            space()
            for x in range(len(modelList)):
                print("{}.)  '{}'".format(x, modelList[x]))
            space()
            modelSelect = input(
                "Please select the index according to your model name: [0|{}]  ".format(len(modelList) - 1))
    except IndexError:
        print("Your selection was out of the model list range.")
        modelSelect = input("Please select the index according to your model name: [0|{}]  ".format(len(modelList) - 1))
        pass

