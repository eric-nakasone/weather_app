"""
Function to connect and insert data to Database MongoDB
"""
import pymongo
import certifi

username = 'weather_application'
password = 'T6c94D0EYWVXOJLC'
cluster = 'weathercluster'
port = '27017'

        
def save_to_db(data):
    """ Definition of function to save data in Database"""
        
    connection_string = f'mongodb+srv://{username}:{password}@{cluster}.mcqcbpx.mongodb.net/'

    client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())

    weather_db = client["weather_application"]

    collection_name = "weather_app"

    collection = weather_db[collection_name] 
    collection.insert_many(data)

    print("Succeeded!")
    
    client.close()