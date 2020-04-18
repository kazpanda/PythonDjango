# Django-LicenseBoard

掲示板から展開

## Debug 方法

import pdb; pdb.set_trace()

よく使うコマンド
s(tep) ステップイン
n(ext) ステップオーバー
r(eturn) ステップアウト
l(ist) 現在行の前後のソースコードを表示
a(rgs) 現在いる関数の引数を表示
p プリント
c(ont(inue)) 次のブレイクポイントまで実行

## Gitlens 設定

{
"gitlens.codeLens.authors.enabled": false,
"gitlens.codeLens.recentChange.enabled": false,
"gitlens.currentLine.enabled": false
}

## 初期データ
python manage.py loaddata licenses\fixtures\license.json

## Pycharm設定
１ File→Settings→Project:project_name→Project Interpreter
  Project Interpreterの横の設定ボダンをクリックし、Add…を選択します。 
  遷移先の画面で、「existing environment」を選択し、Base Interpreterの横の…をクリックし、
  使用しているvenvのpythonのパスを指定します。（Anaconda/envs/env名/python）


２ Run/Debug設定を追加
  設定画面を開く
  メニュー> Run > Edit Configurations..　を選択。
  設定の追加
  「＋」ボタンからPythonを選択
  Name：設定の名称
  Script Path：manage.pyファイルを選択する
  Parameters："runserver"と記入

