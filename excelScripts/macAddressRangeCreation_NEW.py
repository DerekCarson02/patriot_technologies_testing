# Script created by Derek Carson, Lab Technician, Patriot Technologies
import os.path
from openpyxl import Workbook
import sys
import datetime as dt

# Final product directory
filePath = r'Z:\Enterasys - Extreme\MAPPING'
# Removing MAC address standard characters ":", "-"
illegal_chars = {58: "", 45: ""}
datetime_object = dt.datetime.now()


def createMacDocument(newfileName, mac_Address_List):
    destination_filename_path = r'{}\{}.xlsx'.format(filePath, newfileName)
    fileCheck = os.path.exists(destination_filename_path)
    year = datetime_object.year
    workweek = datetime_object.isocalendar().week
    year2string = str(year)

    # Checking if file already exists
    if fileCheck:
        print("{} already exists in this folder! DO NOT overwrite existing files!".format(newfileName))
        sys.exit()

    wb = Workbook()

    # Creating worksheet.
    ws1 = wb.active
    ws1.title = newfileName
    ws1['A1'] = newfileName
    ws1['C1'] = '4120C'
    ws1['A3'] = "FG SN#"
    ws1['B3'] = "MBSN"
    ws1['C3'] = "Admin MAC"
    ws1['D3'] = "TANUM"
    ws1['E3'] = "Chassis"
    ws1['F3'] = "MCX516A-GCAT"
    ws1['G3'] = "480 SSD"
    ws1['H3'] = "1.92 SSD"
    ws1['I3'] = "Extreme MAC"

    for y in range(0, len(mac_Address_List)):
        value = mac_Address_List[y]
        ws1['I{}'.format(y + 4)] = value
        # Serial number generation
        if y+1 >= 10:
            if workweek < 10:
                ws1['A{}'.format(y + 4)] = "XC01" + str(year2string[2:]) + "0" + str(workweek) + "P" + "-700" + str(y+1)
            else:
                ws1['A{}'.format(y + 4)] = "XC01" + str(year2string[2:]) + str(workweek) + "P" + "-700" + str(y+1)
        else:
            if workweek < 10:
                ws1['A{}'.format(y + 4)] = "XC01" + str(year2string[2:]) + "0" + str(workweek) + "P" + "-7000" + str(y+1)
            else:
                ws1['A{}'.format(y + 4)] = "XC01" + str(year2string[2:]) + str(workweek) + "P" + "-7000" + str(y+1)

    wb.save(filename=destination_filename_path)
    print("File located in " + destination_filename_path + " created.")


def workOrderPrompt():
    while True:
        workOrder = input("Please enter your work order number: ")
        if workOrder.isalpha():
            print("This field does not accept letters!")
            pass
        elif len(workOrder) == 0:
            print("Please enter something into the prompt.")
            pass
        elif len(workOrder) > 4:
            print("This field has a character limit of 3!")
            pass
        elif len(workOrder) < 3:
            print("At least 3 or 4 characters should be used for this field!")
            pass
        elif len(workOrder) == 4:
            return "WO0000" + workOrder
        else:
            return "WO00000" + workOrder


# Specified start MAC address prompt
def startMACPrompt():
    while True:
        startMac = input("Please enter your starting MAC address: ")
        if len(startMac) == 0:
            print("Please enter something into the prompt.")
            pass
        elif len(startMac) > 17:
            print("This field has a character limit of 17!")
            pass
        elif len(startMac) < 17:
            print("Mac Addresses are 17 characters! Please enter a valid address!")
            pass
        else:
            return str(startMac)


# Specified end MAC address prompt
def endMACPrompt():
    while True:
        endMac = input("Please enter your ending MAC address: ")
        if len(endMac) == 0:
            print("Please enter something into the prompt.")
            pass
        elif len(endMac) > 17:
            print("This field has a character limit of 17!")
            pass
        elif len(endMac) < 17:
            print("Mac Addresses are 17 characters! Please enter a valid address!")
            pass
        else:
            return str(endMac)


# Master list of mac addresses
def master_Mac_List():
    mac_list = []
    print('Generating MAC address list, this will take a few seconds...\r')
    # Extreme MAC stamp
    mac = 'C8:66:5D:'
    # Generating master MAC address list based on Extreme standards
    for number in range(16 ** 6):
        hex_num = hex(number)[2:].zfill(6)
        mac_list.append("{}{}{}:{}{}:{}{}".format(mac.upper(), *hex_num.upper()))
    return list(mac_list)


# Mac addresses inside the mac range
def mac_Range_List(master_mac, start_mac, end_mac):
    mac_range = []
    start = 0
    end = 0
    # Assigning the start and end indexes according to specified MAC address range
    for x in range(len(master_mac)):
        if master_mac[x] == start_mac:
            start = x
        if master_mac[x] == end_mac:
            # Including the final address
            end = x + 1
    for n in range(start, end):
        mac_range.append(master_mac[n])
    return list(mac_range)


# Mac addresses that will be mapped into the work order.
def final_Output_Mac_List(mac_range):
    mapped_mac_addresses = []
    out_list = []
    for w in range(len(mac_range)):
        # Mapping every 65th address
        if (w % 64) == 0:
            mapped_mac_addresses.append(mac_range[w])
    # Removing ":" character from address per Extreme specifications
    for item in mapped_mac_addresses:
        out_list.append(item.translate(illegal_chars))
    return list(out_list)


# Assigning variables
master_address_list = master_Mac_List()
address_file_name = workOrderPrompt()
first_Address = startMACPrompt()
last_Address = endMACPrompt()

createMacDocument(address_file_name.translate(illegal_chars),
                  final_Output_Mac_List(mac_Range_List(master_address_list, first_Address, last_Address)))

