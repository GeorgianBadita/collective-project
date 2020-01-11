from app.models.validators.Exceptions import MyException
from app.models.validators.Validator import Validator
from datetime import datetime


class DonationValidator(Validator):
    @staticmethod
    def validate(entity):
        errors = []
        current_time = datetime.now()
        donation_date = entity.date

        if not isinstance(donation_date, datetime):
            raise MyException("Donation date is invalid!")

        if current_time > donation_date:
            errors.append("Donations can't be done in the past!")

        if entity.donor_id is None:
            errors.append("Donor id can't be null!")

        if len(errors) > 0:
            raise MyException("\n".join(errors))
