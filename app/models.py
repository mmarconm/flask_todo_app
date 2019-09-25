from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure_db(app):
    db.init_app(app)
    app.db = db


class Todo(db.Model):
    id = db.Column(
        db.Integer,
        unique=True,
        primary_key=True
    )
    task = db.Column(db.String(300))
    pub_date = db.Column(
        db.DateTime, nullable=False,
        default=datetime.utcnow
    )

    def __str__(self):
        return str(self.task)

    def __repr__(self):
        return str(self.task)
