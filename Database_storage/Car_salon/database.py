import sqlite3

CREATE_TABLE ="CREATE TABLE IF NOT EXISTS car_salon (id INTEGER PRIMARY KEY, name TEXT, type TEXT, price INTEGER);"

INSERT_CAR = "INSERT INTO car_salon (name, type, price) VALUES (?, ?, ?);"
GET_ALL_CARS = "SELECT * FROM car_salon;"
GET_CARS_BY_NAME = "SELECT * FROM car_salon WHERE name = ?"

def connect():
    return sqlite3.connect('data.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def add_a_car(connection, name, type, price):
    with connection:
        return connection.execute(INSERT_CAR, (name, type, price))

def fetch_all(connection):
    with connection:
        return connection.execute(GET_ALL_CARS).fetchall()

def get_car_by_name(connection, name):
    with connection:
        return connection.execute(GET_CARS_BY_NAME, (name,)).fetchall()

