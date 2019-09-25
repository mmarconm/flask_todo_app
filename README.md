# TODO APP

## Use virtualenv para essa aplicacao

```sh
python -m venv env

# linux
source env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development # debug mode

# windows
env\Script\activate
set FLASK_APP=app
set FLASK_ENV=development

# depois instale as bibliotecas necessarias
pip install flask flask-sqlalchemy flask-migrate

# ou usando requirements.txt para instalar versao especificas
pip install -r requirements.txt

```

## Bootstrap 4.3.1

```
Nesse projeto estou usando bootstrap 4 usando CDN
```

## Rodar o projeto

```
flask run 
```