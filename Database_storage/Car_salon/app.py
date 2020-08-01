from Database_storage.Car_salon import database

MENU_PROMPT = """
1)Add a new car.
2)See all avalable cars.
3)Find a car by name.
4)Exit.

Your selection:

"""

def main():
    connection = database.connect()
    database.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "4":
        if user_input == "1":
            name = input("Enter cars name: ")
            type = input("Enter what does it run with gas/diesel or is it electric: ")
            price = input("How much does it cost($): ")
            database.add_a_car(connection, name, type, price)
        elif user_input == "2":
            cars = database.fetch_all(connection)

            for car in cars:
                print(f"The model is {car[1]} it runs at {car[2]} and the price is {car[3]} $")
        elif user_input == "3":
            name = input("Enter cars name to find: ")
            cars = database.get_car_by_name(connection, name)

            for car in cars:
                print(f"Found the car  {car[1]} it runs at {car[2]} and the price is {car[3]} $")
        else:
            print("Wrong input please try again!")




main()