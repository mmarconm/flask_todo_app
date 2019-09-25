from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
DB = path.join(BASE_DIR, 'database.db')


class Config:
    DEBUG = True
    SECRET_KEY = 'adminadmin'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
