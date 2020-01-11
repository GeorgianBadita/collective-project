from datetime import datetime, timedelta

import pytest
from app.models.models import User, Donation
from app.models.validators.DonationValidator import DonationValidator
from app.models.validators.Exceptions import MyException
from app.models.validators.UserValidator import UserValidator


class TestValidators:
    """
    Function to test validators class
    """

    def test_user_validator(self):
        u = User(user_id='1824121ajfh', username='gabi', email='gabi@g.com', phone_number='+40 0752823713',
                 blood_group_id=1, national_id='19907123512', diseases='', about='', profile_pic='')
        validator = UserValidator()
        try:
            validator.validate(u)
            assert True
        except MyException as e:
            assert False
        u = User(user_id='1824121ajfh', username='gabi', email='gabig.com', phone_number='+40 0752823713',
                 blood_group_id=1, national_id='19907123512', diseases='', about='', profile_pic='')
        try:
            validator.validate(u)
            assert False
        except MyException as e:
            assert "Email format is incorrect!" in e.get_errors()
            assert True

        u = User(user_id='1824121ajfh', username='gabi', email='gabig.com', phone_number='+40 0752823713',
                 blood_group_id=10, national_id='19907123512', diseases='', about='', profile_pic='')
        try:
            validator.validate(u)
            assert False
        except MyException as e:
            assert "Email format is incorrect!" in e.get_errors()
            assert "Blood group is invalid!" in e.get_errors()
            assert True

        u = User(user_id='1824121ajfh', username='gabi', email='gabi@g.com', phone_number='+0[752823713',
                 blood_group_id=1, national_id='19907123512', diseases='', about='', profile_pic='')

        try:
            validator.validate(u)
            assert False
        except MyException as e:
            assert "Incorrect phone number!" in e.get_errors()
            assert True

    def test_donation_validator(self):
        date = datetime.now() + timedelta(days=1)
        d = Donation(donor_id=1, date=date)
        donation_validator = DonationValidator()
        donation_validator.validate(d)

    def test_blood_request_validator(self):
        pass
