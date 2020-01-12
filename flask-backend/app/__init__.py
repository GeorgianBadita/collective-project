from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager
db = SQLAlchemy()  # our database
login_manager = LoginManager()


@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403


@login_manager.user_loader
def load_user(user_id):
    u = User.query.get(user_id)
    print(user_id, u, "////////////////////////////////")
    return u


def create_app(config_class=Config):
    """
    Function to create the application
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    from app.models.models import UserLogin
    # blueprint for the auth routes
    from .auth.routes import bp_auth
    app.register_blueprint(bp_auth)
    from .http.api import bp_api
    app.register_blueprint(bp_api)
    return app


from app.models.models import *
