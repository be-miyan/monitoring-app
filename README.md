# monitoring-app
自宅でラズパイから収集した情報(気温や画像など）をDBに登録してwebで表示するアプリを作って見た
djangoを初めて触ってゴリゴリ書いたソースなのでまだまだリファクタリングの余地あり

## django/

django application   
情報登録・表示アプリ  
(詳細は django/README.md 参照)

## script/

data send script  
ラズパイ上で動かすデータ送信用スクリプト

## motion.conf

motionを使用する場合の参考設定  
画像をAPIにcurlで送信しています
(motionは動体検知用パッケージ。ラズパイなどにインストール)

~~~ bash
sudo apt-get install motion
~~~
