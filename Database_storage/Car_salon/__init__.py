import sqlite3

def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS car_salon (id INTEGER PRIMARY KEY, name TEXT, type TEXT, price INTEGER);"
            )

