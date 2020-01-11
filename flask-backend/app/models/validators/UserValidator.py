import re

from app.models.validators.Validator import Validator


class UserValidator(Validator):

    @staticmethod
    def validate(entity):
        if len(entity.username) > 256:
            return False

        if not re.match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', entity.mail):
            return False

        if not entity.blood_group in (1, 2, 3, 4):
            return False

        return True

