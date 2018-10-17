# coding: utf-8
from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.test_db
collection = db.test_collection

results = collection.find()

for result in results:
    print(result)
result = collection.insert_one({"id": 1, "name": "tetsufe"})
