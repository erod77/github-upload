import pymongo


class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['test']

    @staticmethod
    def insert(collections, data):
        Database.DATABASE[collections].insert(data)

    @staticmethod
    def find(collections, query):
        Database.DATABASE[collections].find(query)

    @staticmethod
    def find_one(collections, query):
        Database.DATABASE[collections].find_one(query)