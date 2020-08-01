import pymongo
import sys

client = pymongo.MongoClient("mongodb+srv://Richard:Asebomu12@cluster0-xth9g.mongodb.net/Richard?retryWrites=true&w=majority")

db = client.get_database('total_records')

user_info = db.user_info

#print(list(user_info.find()))


running = True

def main():
    
    first_input = input("Do you want to enter a new User? (y/n) ")
    if first_input.lower() == 'y':
        name = str(input('Enter your name: '))
        surname = str(input('Enter your last name: '))
        try:
            phone = int(input('Enter your number: '))
        except ValueError:
            print("Only number values allowed!")

        while True:
            list_values = []
            entry = str(input('Enter a profession/hobby (q to quit): '))
            if entry.lower() == 'q':
                sys.exit()
            list_values.append(entry)
        user_input = {"first_name": name, "last_name": surname, "cell": phone, "profession/hobbies": list_values}
        
        user_info.insert_one(user_input)
    elif first_input.lower() == 'n':
        print('Ok understood')
        sys.exit()
    

main()
