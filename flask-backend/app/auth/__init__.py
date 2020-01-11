from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes




# Internal imports
from app.auth.db import init_db_command
from app.auth.user import User

