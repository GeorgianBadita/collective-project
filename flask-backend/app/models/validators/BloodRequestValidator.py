from app.models.validators.Exceptions import MyException
from app.models.validators.Validator import Validator


class BloodRequestValidator(Validator):

    @staticmethod
    def validate(entity):
        errors = []
        if entity.blood_group_id not in range(9):
            errors.append("Invalid blood group!")
        if len(errors) > 0:
            raise MyException("\n".join(errors))

