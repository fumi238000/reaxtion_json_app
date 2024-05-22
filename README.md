# README

## デプロイ

https://reaxtionjsonapp-vb5bmyoqhvffbfxzchfksw.streamlit.app/

streamlit の環境を作成するテンプレート

## setup

```shell
git clone
cd
docker-compose build
docker-compose up -d
```

立ち上がれば ok

- http://localhost:8501/

## 課題

- あれば追加する

## メモ

起動しなかったので、logs を吐き出す方法を知った。これは多様したい。

```shell
 docker-compose logs
```

## 値メモ

```shell
# センサー
sensor
センサー(近距離)": 0
"センサー(遠距離)" 1
"タッチ(敏感)": 2
"タッチ(鈍感): 3

# 論値
logic
全て: 1
任意: 0
```
