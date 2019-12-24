from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    Class for representing our User model
    @id - primary key column
    @email - user's email
    @password - user's password
    @name - username
    """
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(1024))
    email = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256))

    def __repr__(self):
        return '<User name: {}, email: {}'.format(self.username, self.email)
