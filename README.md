# コンテナの起動
```
docker-compose up -d
```

## コンテナ起動確認

```
docker-compose ps
```

# mongo-expressへアクセス
DBの中をブラウザで見れる
```
http://0.0.0.0:8081/
```

# mongoDBコマンド実行

```
docker-compose exec mongo bash
mongo admin -u root -p
<docker-compose.yamlに記載したパスワードを入力。デフォルトは"admin">
```

testデータベースのhogeテーブルにレコードを追加して確認するサンプル
```
show databases
use test
db.hoge.insert({ name: "test" })
db.hoge.find()
exit
```

# Python実行
コンテナへ接続
```
docker exec -it python3 bash
cd app
python helloworld.py
```


# 閉める
```
docker-compose down
```
