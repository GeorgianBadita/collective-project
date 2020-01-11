from app.models.repository.AbstractRepository import AbstractRepository
from app.models.models import BloodRequest
from app.models.validators.BloodRequestValidator import BloodRequestValidator


class BloodRequestRepository(AbstractRepository):

    def __init__(self):
        validator = BloodRequestValidator()
        super().__init__(validator, BloodRequest)
