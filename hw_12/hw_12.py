
import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection= sqlite3.connect(":memory:")
        print("Соединение установлено")
    except Error as e:
        print(f" Ошибка соединения '{e}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен")
    except Error as e:
        print(f"Ошибка запроса '{e}' ")



def execute_read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

