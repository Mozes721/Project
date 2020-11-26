import pymongo

#connect to the MongoDB

client = pymongo.MongoClient("mongodb+srv://Username:Password@cluster0-xth9g.mongodb.net/Richard?retryWrites=true&w=majority")

db = client.get_database('total_records')
records = db.car_record


cars = [ {'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]


updated = {'price': 8500}
car = {'name': 'BMW', 'price': 20100}

#updating
records.update_one({'name': 'Skoda'}, {'$set': updated})


#deleteing
records.delete_one({'name': 'BMW'})
print(list(records.find())
