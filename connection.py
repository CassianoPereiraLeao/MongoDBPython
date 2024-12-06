from pymongo import MongoClient
from .mongodb_configs import mongo_db_infos

class DbConnectionHandler:
    def __init__(self) -> None:
        self._connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            mongo_db_infos['USER'],
            mongo_db_infos['PASSWORD'],
            mongo_db_infos['HOST'],
            mongo_db_infos['PORT']
        )
        self._db_name = mongo_db_infos['DATABASE']
        self._client = None
        self._db_connection = None
    
    def connect_to_db(self):
        self._client = MongoClient(self._connection_string)
        self._db_connection = self._client[self._db_name]
    
    def get_db_connection(self):
        return self._db_connection
    
    def get_db_client(self):
        return self._client
