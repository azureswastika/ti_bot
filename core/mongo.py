from typing import Any

from pymongo import MongoClient
from pymongo.collection import Collection


class Mongo:
    def __init__(
        self, host: str = None, port: int = None, *, database: str = "main"
    ) -> None:
        self.client = MongoClient() if host and port else MongoClient(host, port)
        self.database = self.client[database]

    def get_collection(self, name: str):
        return MongoCollection(self.database[name])


class MongoCollection:
    def __init__(self, collection: Collection) -> None:
        self.collection = collection

    def create(self, data: dict[str, Any]):
        return self.collection.insert_one(data).inserted_id

    def get(self, ffilter: dict):
        return self.collection.find_one(ffilter)

    def select(self, ffilter=dict()):
        return [data for data in self.collection.find(ffilter)]

    def update(self, ffilter: dict, update: dict):
        return self.collection.update_one(ffilter, update)


mongo = Mongo()
tickers = mongo.get_collection("tickers")
