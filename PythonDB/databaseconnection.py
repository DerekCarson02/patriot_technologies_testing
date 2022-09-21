import mysql.connector
from mysql.connector import Error


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


create_server_connection("10.10.0.28", 'Administrator', 'sDaD12v!')
patriot_main_db = connection_patriot_main = create_db_connection("10.10.0.28", "Administrator", "sDaD12v!", "patriot_technologies_main")