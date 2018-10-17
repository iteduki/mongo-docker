# coding: utf-8
from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.test_db
collection = db.test_collection

# dbの全削除
collection.drop()

# 100万件のレコード
collection.insert_many([{"id": i}for i in range(1000000)])

# idが1のものを探す
results = collection.find({"id": 1})

for result in results:
    print(result)
