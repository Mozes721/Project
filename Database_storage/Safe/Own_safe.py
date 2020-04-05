import cv2
import imageio
import sqlite3
import base64
import os

PASSWORD = "Everest"

connect = input("Enter your password?\n")

while connect != PASSWORD:
    connect = input("Enter your password?\n")
    if connect == "q":
        break

if connect == PASSWORD:
    conn = sqlite3.connect('storage.db')

    try:
        conn.execute('''CREATE TABLE SAFE
        (FULL_NAME TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        EXTENSION TEXT NOT NULL,
        FILES TEXT NOT NULL)
        ''')

        print("Your safe has been created")
    except:
        print("You already have a safe")

    while True:
        print("\n" + "*"*15)
        print("Given comands")
        print("q = quit program")
        print("o = open file")
        print("s = store file")
        print("*"*15)
        input_ = input(":")

        if input_ == "q":
            break
        if input_ == "o":
            file_type = input("What is the filetype of the file you want to open?\n")
            file_name = input("What is the name of the file you want to open?\n")
            FILE = file_name + "." + file_type

            cursor = conn.execute("SELECT * from SAFE WHERE FULL_NAME= " + '"' + FILE + '"')

            file_string = ""

            for row in cursor:
                file_string = row[3]
            with open(FILE, 'wb') as f_output:
                print(file_string)
                f_output.write(base64.b64decode(file_string))


        if input_ == "s":
            PATH = input("Type in the full path to the file you want to store.\nExample: /Users/mark/Desktop/somefile.py\n")


            FILE_TYPES = {
                "txt": "TEXT",
                "java": "TEXT",
                "dart": "TEXT",
                "py": "TEXT",
                "jpg": "IMAGE",
                "png": "IMAGE",
                "jpeg": "IMAGE"
            }

            file_name = PATH.split("/")
            file_name = file_name[len(file_name) - 1]
            file_string = ""

            NAME = file_name.split(".")[0]
            EXTENSION = file_name.split(".")[1]

            try:
                EXTENSION = FILE_TYPES[EXTENSION]
            except:
                Exception()

            if EXTENSION == "IMAGE":
                IMAGE = cv2.imread(PATH)
                file_string = base64.b64encode(cv2.imencode('.jpg',IMAGE)[1]).decode()
            
            elif EXTENSION == "TEXT":
                file_string = open(PATH, "r").read()
                file_string = base64.b64encode(file_string)

            EXTENSION = file_name.split(".")[1]

            command = 'INSERT INTO SAFE (FULL_NAME, NAME, EXTENSION, FILES) VALUES (%s, %s, %s, %s);' %('"' + file_name +'"', '"' + NAME +'"', '"' + EXTENSION +'"', '"' + file_string +'"')
            
            conn.execute(command)
            conn.commit()

