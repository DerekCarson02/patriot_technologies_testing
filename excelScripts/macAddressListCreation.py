# Script created by Derek Carson, Lab Technician, Patriot Technologies
import os.path
from openpyxl import Workbook
import sys
import datetime as dt

# Final product directory
filePath = r'Z:\Enterasys - Extreme\4120C Mac Addresses'
# Removing MAC address standard characters ":", "-"
illegal_chars = {58: "", 45: ""}
datetime_object = dt.datetime.now()


def createMacDocument(newfileName, mac_Address_List):
    destination_filename_path = r'{}\{} Mac Address Request.xlsx'.format(filePath, newfileName)
    fileCheck = os.path.exists(destination_filename_path)
    # Checking if file already exists
    if fileCheck:
        print("{} already exists in this folder! DO NOT overwrite existing files!".format(newfileName))
        sys.exit()

    wb = Workbook()

    # Creating worksheet.
    ws1 = wb.active
    ws1.title = newfileName
    ws1['A1'] = "Extreme MAC Request Sheet"
    ws1['A3'] = "Extreme MAC"

    for y in range(0, len(mac_Address_List)):
        value = mac_Address_List[y]
        ws1['A{}'.format(y + 4)] = value

    wb.save(filename=destination_filename_path)
    print("File located in " + destination_filename_path + " created.")


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
def master_Mac_List(start_mac):
    mac_list = []
    print('Generating MAC address list, this will take a few seconds...\r')
    # Extreme MAC stamp
    mac = start_mac[0:9]
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
first_Address = startMACPrompt()
master_address_list = master_Mac_List(first_Address)
last_Address = endMACPrompt()

createMacDocument(first_Address.translate(illegal_chars),
                  final_Output_Mac_List(mac_Range_List(master_address_list, first_Address, last_Address)))

