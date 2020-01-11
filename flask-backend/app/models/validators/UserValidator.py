import re

from app.models.validators.Exceptions import MyException
from app.models.validators.Validator import Validator


class UserValidator(Validator):

    @staticmethod
    def validate(entity):
        errors = []
        if len(entity.username) > 256:
            errors.append("Username can't be longer than 256 characters!")

        if not re.match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', entity.email):
            errors.append("Email format is incorrect!")

        if not entity.blood_group_id in (1, 2, 3, 4, 5, 6, 7, 8):
            errors.append("Blood group is invalid!")

        if not re.match(r'((?:\+|00)[17](?: |\-)?|(?:\+|40)[1-9]\d{0,2}'
                        r'(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|'
                        r'[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)'
                        r'[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))', entity.phone_number):
            errors.append("Incorrect phone number!")

        if len(errors) > 0:
            raise MyException('\n'.join(errors))
