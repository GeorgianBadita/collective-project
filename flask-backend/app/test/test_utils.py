import os
import pytest
from flask import Flask

from app import db, User
from app.utils.utils import populate_blood_group_table, generate_random_users, generate_random_donations, \
    generate_random_blood_requests

basedir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    db.init_app(app)
    with app.app_context():
        db.create_all()
        populate_db()
        yield app  # Note that we changed return for yield, see below for why
        db.drop_all()


def populate_db():
    u = User(user_id='18241211ajfh', username='gabii', email='gabii@g.com', phone_number='+40 0752823713',
             national_id='19907123512', diseases='asd', about='das', profile_pic='1', profile_setup=True)
    db.session.add(u)
    db.session.commit()
    populate_blood_group_table(db)
    users = generate_random_users(100)
    for user in users:
        db.session.add(user)
        db.session.commit()
    donations = generate_random_donations(100)
    for donation in donations:
        db.session.add(donation)
        db.session.commit()
    blood_requests = generate_random_blood_requests(100)
    for blood_request in blood_requests:
        db.session.add(blood_request)
        db.session.commit()
