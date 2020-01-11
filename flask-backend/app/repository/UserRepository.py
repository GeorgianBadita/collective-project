from app.repository.AbstractRepository import AbstractRepository
from app.models.models import User
from app.models.validators.UserValidator import UserValidator


class UserRepository(AbstractRepository):

    def __init__(self):
        validator = UserValidator()
        super().__init__(validator, User)
