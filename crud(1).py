from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30907
        DB = 'AAC'
        COL = 'animals'

        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client[DB]

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        if query is not None:
            return list(self.database.animals.find(query))
        else:
            raise Exception("Query parameter is empty")

    def update(self, query, new_values):
        if query is not None:
            result = self.database.animals.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            raise Exception("Query parameter is empty")

    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter is empty")
