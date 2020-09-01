## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
```

## install requirements

```bash
pip install -r requirements.txt

# if you ran into any issue with kerbrose package install below system dependencies
sudo apt-get install krb5-config libkrb5-dev libssl-dev libsasl2-dev libsasl2-modules-gssapi-mit python3.7-dev python3-dev -y

```

## running django management commands & usage

```sh
source .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## mysql details path file should contain and set path accordingly in workindia_test/settings.py file's DATABASES

database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
