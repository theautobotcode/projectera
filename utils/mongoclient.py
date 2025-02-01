from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = f"mongodb://{os.getenv('USERNAME','')}:{os.getenv('PASSWORD','')}@{os.getenv('HOST','')}/?retryWrites=true&w=majority&appName=Cluster0"

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client['projectera']

    def insert(self, collection, data):
        self.db[collection].insert_one(data)

    def find(self, collection, query):
        return self.db[collection].find(query)

    def update(self, collection, query, data):
        self.db[collection].update(query, data)

    def delete(self, collection, query):
        self.db[collection].remove(query)
