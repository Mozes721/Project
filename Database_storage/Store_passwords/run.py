import sys
import base64
from Database_storage.Store_passwords import db
import secrets
import string

ADMIN_PASS = 'qwerty'



connect = input("What is your password?\n")




while ADMIN_PASS != connect:
    connect = input("What is your password?\n")
    if connect == 'q':
        break
def create_password(lenghts):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(lenghts))
    encrypt_password(password)
    return password

def encrypt_password(pwd):
    # make a hashing string
    h = hashlib.md5(pwd.encode())
    return h




if connect == ADMIN_PASS:
    try:
        db.insert()
        print("Your pwd safe has been created!")
    except:
        print("You already have a safe")

    while True:
        print("\n" + "*" * 15)
        print("Avalable commands")
        print("i = generate new password")
        print("l = list current avalable platforms")
        print("f = fetch specific password")
        print("d = delete specific password/platform")
        print('q = quit program')
        print("\n" + "*" * 15)

        inputval = input(':')

        if inputval == 'i':
            platform = input('What platform do you want to insert in?')
            pass_generator = int(input('What lenght do you want it to be?'))
            create_password(pass_generator)

            db.insert(platform, create_password(pass_generator))

        if inputval == 'l':
            db.view_platforms()

        if inputval == 'f':
            find_value = input('what value you want to find:')
            db.view_pass(find_value)

        if inputval == 'd':
            del_value = input('what value you want to delete:')
            db.delete_one(del_value)

        if inputval == 'q':
            break



