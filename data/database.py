from pymongo import MongoClient


class DB(object):
    # set host and port
    client = MongoClient(host='localhost', port=27017)
    # set database name client['database name']
    db_name = client['Trip']
    # set collection name db_name['collection name']
    # db = db_name['WebAdmin']

    @staticmethod
    def init(collection):
        DB.db = DB.db_name[collection]
        return DB.db

    @staticmethod
    def inset(data):
        DB.db.insert(data)

    @staticmethod
    def get_all(collection):
        db = DB.init(collection)
        return db.find({}, {'_id': 0, 'password': 0})

    @staticmethod
    def modify_state(collection, id_trip, state):
        db = DB.init(collection)
        db.find_one_and_update({'id_trip': id_trip}, {'$set': {'state': state}})

    @staticmethod
    def modify_user(collection, username, data):
        db = DB.init(collection)
        db.update_one({'username': username}, {'$set': data})

