from flask import Flask
from flask_migrate import Migrate
# local imports
from app.config import Config
from app.models import configure_db


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # configure dd
    configure_db(app=app)

    # set migrate to use with flask db init
    Migrate(app, app.db)

    # register blueprints
    from app.views import task
    app.register_blueprint(task)

    return app
