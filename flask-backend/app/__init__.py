from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager

db = SQLAlchemy()  # our database


def create_app():
    """
    Function to create the application
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from app.models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        """
        @param: user_id - primary key from the User table
        """
        return User.query.get(int(user_id))

    # blueprint for the auth routes
    from .auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth routes
    from .routes.routes import route as route_blueprint
    app.register_blueprint(route_blueprint)

    return app


from app.models.models import *