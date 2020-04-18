# よく使うコマンド

## 仮想インストール
* pip3 install --upgrade pip
* pip3 install virtualenv

## 仮想環境の作成
* virtualenv ENV
* python3 -m virtualenv ENV
* source ENV/bin/activate

## Djangoのインストール
* pip3 install django
* pip install django-bootstrap-form
* pip install django-debug-toolbar

## プロジェクトを作成する
* ドットを付けて実行する（余計にフォルダーが作られる）
* django-admin startproject todoproject .

## アプリを作成する
* python3 manage.py startapp todo

## 中間ファイルを作る
* python3 manage.py makemigtarions

## DBを更新する
* python3 manage.py migrate
* python3 manage.py makemigrations --fake
* python3 manage.py makemigrations
* python3 manage.py migrate

## スーパーユーザーの作成
* python3 manage.py createsuperuser

## サーバーを起動する
* python3 manage.py runserver

## 備忘録
* migrateが効かないときは、dbファイルを削除する


# VSCodeの設定
* エラー対策
~~~
    {
        "git.ignoreLimitWarning": true,
        "python.pythonPath": "ENV_W\\Scripts\\python.exe",
        "python.venvFolders": [
        "${workspaceFolder}\\ENV_W"
    ]
    }
~~~

