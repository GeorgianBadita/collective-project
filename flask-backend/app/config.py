import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Class to configure the application
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'randomKey123'  # SECRET KEY for encryption
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # database location
    SQLALCHEMY_TRACK_MODIFICATIONS = False