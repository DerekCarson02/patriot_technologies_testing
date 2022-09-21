import mysql.connector
from mysql.connector import Error
from os.path import exists
import pandas as pd
import datetime as dt

deletechars = {44: "", 34: "", 40: "", 41: "", 39: ""}
space = {32: ""}
today = dt.datetime.now()
mydate = {}
mydate['day'] = today.day
mydate['month'] = today.month
mydate['year'] = today.year
mydate['hour'] = today.hour


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection as '{}'@'{}' successful!".format(user_name, host_name))
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection to {} as {} successful!".format(db_name, user_name))
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_data(table):
    describeTable = """DESCRIBE {}""".format(table)
    table_info = read_query(connection_patriot_main, describeTable)
    table_fields = {}
    print("Accessing '{}' table info...\r".format(table))
    for i in range(len(table_info)):
        print(table_info[i])
        tupleToString = table_info[i]

        split0 = str(tupleToString).split(",")[0]
        split1 = str(tupleToString).split(",")[1]

        field_name = split0.translate(deletechars)
        field_type = split1.translate(deletechars).translate(space)

        print("{} | {}".format(field_name.upper(), field_type.upper()))
        if field_type == "BINT":
            table_fields[field_name] = 0
        elif field_type == "BVARCHAR255":
            table_fields[field_name] = """"""
        else:
            table_fields[field_name] = ""
    for item in table_fields:
        if item == "created_at":
            table_fields[item] = ("{}/{}/{}".format(mydate['month'], mydate['day'], mydate['year']))
            continue
        table_fields[item] = (input("Please enter {} attribute information: ".format(item.upper())))
    print(table_fields)

show_Tables = """SHOW TABLES;"""

create_server_connection("10.10.0.28", 'Administrator', 'sDaD12v!')
connection_patriot_main = create_db_connection("10.10.0.28", "Administrator", "sDaD12v!", "patriot_technologies_main")
table_names = read_query(connection_patriot_main, show_Tables)
table_array = []
for result in table_names:
    result = str(result)
    table_array.append(result)

describeTable = """"""
table_info = """"""
for x in range(len(table_array)):
    describeTable = """DESCRIBE {}""".format(table_array[x].translate(deletechars))
    table_info = read_query(connection_patriot_main, describeTable)
    # if exists('C:/Users/dcarson/Documents/test.txt'):
    # open('C:/Users/dcarson/Documents/test.txt', 'a').write("\r")
    # open('C:/Users/dcarson/Documents/test.txt', 'a').write(describeTable)
    print(describeTable)
    # open('C:/Users/dcarson/Documents/test.txt', 'a').write("\r")
    for i in range(len(table_info)):
        string = ""
        string = table_info[i]
        # open('C:/Users/dcarson/Documents/test.txt', 'a').write(str(string))
        print(string)
    # else:
    # open('C:/Users/dcarson/Documents/test.txt', 'w').write("--Table Info--\r")

    # if exists('C:/Users/dcarson/Documents/test.txt'):
    #      open('C:/Users/dcarson/Documents/test.txt', 'a').write(table_array[x].translate(deletechars) + "\r")
    # else:
    #     open('C:/Users/dcarson/Documents/test.txt', 'w').write("--Table Info--\r")
print("------------------------" * 2)
