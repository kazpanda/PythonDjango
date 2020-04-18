python manage.py migrate --settings=demo.settings
python manage.py loaddata demo/helloworld/fixtures/helloworld/default_data.json --settings=demo.settings
python manage.py runserver --settings=demo.settings