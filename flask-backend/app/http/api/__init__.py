from flask import Blueprint

bp_api = Blueprint('api', __name__)

from app.http.api import endpoints
