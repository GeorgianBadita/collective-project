from app.repository.AbstractRepository import AbstractRepository
from app.models.models import Donation
from app.models.validators.DonationValidator import DonationValidator


class DonationRepository(AbstractRepository):

    def __init__(self):
        validator = DonationValidator()
        super().__init__(validator, Donation)
