課題
====

課題は順番にこなす必要はありません。面白そうだと思った課題にチャレンジしてみてください。

もちろんこれ以外に自分で課題を持っているならば、それをやってみるのも良いでしょう。

socketモジュールを使ってネットワーク通信
----------------------------------------

1. socketモジュールを使って足し算を行うサーバを作成してください

   telnetコマンドで次のように ``整数+整数`` のように送信すると足し算の結果を返すサーバを作成してください。

   ::

      $ telnet localhost 5000
      Trying 127.0.0.1...
      Connected to debian02.
      Escape character is '^]'.
      10+20
      30
      123+456
      579

.. hint::

   1. socketモジュールのドキュメントの例を参考に、サーバ側で受け取ったテキストを改行位置で分割します("10+20"というデータになります)
   2. 分割したテキストの一つ目の要素を ``+`` でさらに分割します("10"と"20"のデータになります)
   3. 分割したテキストを数値に変換し、足しあわせて、結果を送信します

   http://www.python.jp/doc/release/library/socket.html

2. socketモジュールを使って、1.で作成したサーバにデータを送信して、結果を取得して画面に表示するプログラムを作成してください

   引数を渡して実行すると結果を返してくれるようにしてみてください

   ::

      $ python add.py 10+20
      30

.. hint::

   sysモジュールのargvでコマンドライン引数を取得することができます。

   http://www.python.jp/doc/release/library/sys.html

sqlite3モジュールを使ってデータベース作成
-----------------------------------------

1. sqlite3モジュールを使って、引数で与えられた品名と金額をデータベースに保存するプログラムを作成してください

   ::

     $ python inputdb.py みかん 50
     $ python inputdb.py りんご 100
     $ python inputdb.py バナナ 200

.. hint::

   sysモジュールのargvでコマンドライン引数を取得することができます。

   http://www.python.jp/doc/release/library/sys.html

   sqlite3モジュールでsqlite3のデータベースを操作することができます。

   http://www.python.jp/doc/release/library/sqlite3.html

   :テーブルを作成するSQL: ``CREATE TABLE items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cost INTEGER);``
   :データをテーブルに挿入するSQL: ``INSERT INTO items(name, cost) values("みかん", 50);``

2. 1で作成したデータベースの内容を一覧表示するプログラムを作成してください

   ::

     $ python listdb.py
     みかん 50円
     りんご 100円
     バナナ 200円

.. hint::

   :データを取得するSQL: ``SELECT * FROM items;``

3. 引数から入力された金額以上の品物名とその品物の金額を表示してください

   ::

     $ python filter.py 100
     100円以上の品物は、
     りんご 100円
     バナナ 200円

.. hint::

   :データを取得するSQL: ``SELECT * FROM items WHERE cost >= 100;``
