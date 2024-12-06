from typing import Dict, List

class ConnectionRepository:
    def __init__(self, db_connection) -> None:
        self._collection_name = 'Connect'
        self._db_connetion = db_connection
    
    def insert_document(self, document: Dict) -> Dict:
        collection = self._db_connetion.get_collection(self._collection_name)
        collection.insert_one(document)
        return document

    def insert_multiple_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self._db_connetion.get_collection(self._collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filter) -> List[Dict]:
        collection = self._db_connetion.get_collection(self._collection_name)
        data = collection.find(filter, { '_id': 0})   

        response = list()
        for i in data:
            response.append(i)
        
        return response
    
    def select_one(self, filter) -> Dict:
        collection = self._db_connetion.get_collection(self._collection_name)
        response = collection.filter_one(filter, { '_id': 0})
        return response

    def select_if_exists(self) -> None:
        collection = self._db_connetion.get_collection(self._collection_name)
        data = collection.find({ 'cpf': { '$exists': True } })
        for i in data:
            print(i)
    