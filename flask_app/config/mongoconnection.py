from pymongo import MongoClient

class PyMongo:
    def __init__(self, uri:str):
        self.client = MongoClient(uri)

    def get_database(self, db_name: str):
        return self.client[db_name]


# client = MongoClient('localhost', 27017)
# db= client.biosite_db
# bioproject = db.bioproject
