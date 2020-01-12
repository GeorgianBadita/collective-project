import json

from app import db
from flask_login import UserMixin


class UserLogin(UserMixin, db.Model):
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

    def get_id(self):
        return self.id


class User(UserMixin, db.Model):
    """
    Class for representing our User model
    @user_id - primary key: int
    @username - username: string
    @email - email: string
    @google_id - user google id: string
    @phone_number - user phone number: string
    @blood_group_id - user blood group id: int
    @national_id - user national id: string
    @last_donation_id - id of the last donation made by the user: int
    @diseases - description of the user's diseases: string
    @about - info about the user: string
    @profile_pic - user's profile picture
    @profile_setup - user's setup
    """
    user_id = db.Column(db.TEXT, primary_key=True, autoincrement=False)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(256), default='')
    email = db.Column(db.String(256), unique=True, default='')
    phone_number = db.Column(db.String(20))
    blood_group_id = db.Column(db.Integer, db.ForeignKey('blood_group.blood_group_id', use_alter=True), default=0)
    national_id = db.Column(db.String(20))
    last_donation_id = db.Column(db.Integer, db.ForeignKey('donation.donation_id', use_alter=True), nullable=True)
    diseases = db.Column(db.String(1024))
    about = db.Column(db.String(1024))
    profile_pic = db.Column(db.TEXT)
    profile_setup = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return "<User id: {0}, name: {1}>".format(
            self.user_id, self.username
        )

    def to_map(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "phone_number": self.phone_number,
            "blood_group_id": self.blood_group_id,
            "national_id": self.national_id,
            "last_donation_id": self.last_donation_id,
            "diseases": self.diseases,
            "about": self.about,
            "profile_pic": self.profile_pic,
            "profile_setup": self.profile_setup
        }


class BloodGroup(db.Model):
    """
    Class for representing BloodGroup model
    @id - primary key: int
    @name - group type: string
    @rh - group's rh (+, -): string
    """
    blood_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2), unique=False)
    rh = db.Column(db.String(1), unique=False)

    def __repr__(self):
        return "<Blood Group: id: {0}, name: {1}, rh: {2}>".format(
            self.blood_group_id, self.name, self.rh
        )

    def get_id(self):
        return self.blood_group_id

    def to_map(self):
        return {
            "blood_group_id": self.blood_group_id,
            "name": self.name,
            "rh": self.rh
        }


class BloodRequest(db.Model):
    """
    Class for representing BloodRequest model
    @blood_req_id - primary key: int
    @blood_group_id - foreign key: int
    @location - blood request location: string
    @description - request description: string
    @user_id - user who made the request - foreign key: int
    """
    blood_req_id = db.Column(db.Integer, primary_key=True)
    blood_group_id = db.Column(db.Integer, db.ForeignKey('blood_group.blood_group_id', use_alter=True), nullable=True)
    location = db.Column(db.String(256))
    person_name = db.Column(db.String(256))
    description = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', use_alter=True), nullable=True)

    def get_id(self):
        return self.blood_req_id

    def __repr__(self):
        return "<BloodRequest: id: {0}, user_id: {1}>".format(
            self.blood_req_id, self.user_id
        )

    def to_map(self):
        return {
            "blood_req_id": self.blood_req_id,
            "blood_group_id": self.blood_group_id,
            "location": self.location,
            "person_name": self.person_name,
            "description": self.description,
            "user_id": self.user_id
        }


class Donation(db.Model):
    """
    Class for representing the Donation model
    @donation_id - primary key: int
    @donor_id - foreign key: int
    @date - donation date: DateTime
    @request_id - foreign key: int
    """

    donation_id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.user_id', use_alter=True), nullable=False)
    date = db.Column(db.DateTime)
    request_id = db.Column(db.Integer, db.ForeignKey('blood_request.blood_req_id', use_alter=True), nullable=True)

    def get_id(self):
        return self.donation_id

    def __repr__(self):
        return "<Donation: donation_id: {0}, donor_id: {1}, date: {2}>".format(
            self.donation_id, self.donor_id, self.date
        )

    def to_map(self):
        return {
            "donation_id": self.donation_id,
            "donor_id": self.donor_id,
            "date": self.date,
            "request_id": self.request_id
        }
