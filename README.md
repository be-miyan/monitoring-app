# monitoring-app
自宅でラズパイから収集した情報(気温や画像など）をDBに登録してwebで表示する画面を作って見た。  
djangoを初めて触ってゴリゴリ書いたソースなのでまだまだリファクタリングの余地あり。

※個人用。Djangoのマイグレーション手順や内容の解説は省略します。

## 画面表示

http://[ホスト]/dashboard/home/  

## API (django-rest-framework)

画像登録
http://[ホスト]/dashboard/posts/photo/  
センサー取得データ登録  
http://[ホスト]/dashboard/posts/record/

## TODO

- view fix(def base)
- グラフの文字切れ問題
- model変数名fix(Enviroment -> record)
- app名fix(rpzsensor -> xxx)

## 追加したい機能

- ログインページデザイン
- 画像と取得データを表示する個別ページ（フィルタ機能あり）
- 取得値ごとにページ分ける
- ユーザと取得場所の紐付け
- フッター追加
