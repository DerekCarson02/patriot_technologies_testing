import mysql.connector
from mysql.connector import Error
from databaseconnection import patriot_main_db


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


def read_query_dict(connection, query):
    cursor = connection.cursor(dictionary=True, buffered=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


showTables = """SHOW TABLES"""
test = read_query_dict(patriot_main_db, showTables)
print(test)