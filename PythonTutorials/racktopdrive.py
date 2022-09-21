

menu_options = {
    1: 'List Drive',
    2: 'Select Drive',
    3: 'Select All Drives',
    4: 'Format 4K',
    5: 'Exit',
}


def menu():
    print(menu_options)
    option = int(input('Enter your choice: '))
    while option != 5:
        if option == 1:
            listdrives()
            print(" ")
            menu()
            break
        elif option == 2:
            selectdrive()
            break
        else:
            print("Invalid Option. Retry.")


workingDir = 'C:/Users/dcarson.PATRIOT-TECH/IdeaProjects/PythonTutorials/'
with open('{}testdata.txt'.format(workingDir)) as file:
    lines = file.readlines()

drivelist = []

for x in range(len(lines)):
    if x > 7:
        drivelist.append(" ".join(filter(bool, lines[x].split())))


def selectdrive():

    driveindex = int(input("Please select a drive index: "))

    try:
        brand, devicename, model, serial, fw = drivelist[driveindex].split(' ')
        print('You have selected device name: {}, model: {}, serial number: {}'.format(devicename, model, serial))
        if brand == 'SEAGATE':
            return brand, devicename, model, serial, fw
        elif model[0:2] != 'SP':
            print("This is the RAID controller!")
        else:
            print("This is not a Seagate drive!")
    except IndexError:
        print("The drive you selected is not in the list of drives!")
    except ValueError:
        print("The drive you select is not a Seagate drive!")


def listdrives():
    driveCount=1
    spaceCount=14
    print('{} {} {} {}'.format('Drive Index'.ljust(15), 'Device Name'.ljust(24), 'Model'.ljust(15), 'Serial Number'))
    for x in range(len(drivelist)):
        try:
            brand, devicename, model, serial, fw = drivelist[x].split(' ')
            if model[0:2] != 'SP':
                print('{}.{} {} {} {}'.format(driveCount, "".ljust(spaceCount), devicename.ljust(19), model.ljust(21), serial))
                driveCount+=1
            if driveCount == 10:
                spaceCount = 13
        except ValueError:
            pass


menu()