# coding: utf-8
from pymongo import MongoClient
import json
from operator import itemgetter

client = MongoClient('mongo', 27017)
db = client.test_db
collection = db.test_collection
# テーブルの初期化
collection.drop()

# jsonフォルダのsample.jsonを読み込む
with open('../json/sample.json') as f:
    records = json.load(f)
print(len(records))

# idキーでソートする
records = sorted(records, key=itemgetter('id'))

# 保存する
collection.insert_many(records)
