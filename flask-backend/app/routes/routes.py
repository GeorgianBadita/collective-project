from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app import db

route = Blueprint('route', __name__)


@route.route('/')
def index():
    return render_template('index.html')


@login_required
@route.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)
