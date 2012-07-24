===============================================
Appendix: パッケージ管理ツール
===============================================

Pythonにもサードパーティ製パッケージのリポジトリがあります

http://pypi.python.org/

ここに登録されているパッケージは、パッケージ管理ツールを使って簡単にインストールすることができます。

Pythonのパッケージ管理ツールはいくつか種類がありますが、今回はeasy_installを利用してみます。

インストール
===========================

以下のURLのセットアップ用スクリプトをダウンロードします。

http://python-distribute.org/distribute_setup.py

セットアップスクリプトをsudoで実行します。

.. code-block:: pycon

    $ sudo python distribute_setup.py

これでeasy_installコマンドが使えるようになります。

easy_installを使ってみる
=======================================

試しにipythonをインストールしてみます。

ipythonは高機能なPython対話シェルです。標準のPython対話シェルに比べて補完や多色表示、行番号表示などの便利機能が多数搭載されています。

.. code-block:: pycon

    $ sudo easy_install ipython

これだけでインストールは完了です。ターミナル(コマンドプロンプト)上でipythonと入力してipythonが起動できるか確認してみましょう。
