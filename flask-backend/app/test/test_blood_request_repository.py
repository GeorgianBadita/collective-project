from app.models.models import BloodRequest
from app.repository import DonationRepository, BloodRequestRepository
from datetime import datetime, timedelta
from app.test.test_utils import app


def test_blood_request_repo_add_find_one_find_all(app):
    """
    Function to test blood_request repository add, find_one, find_all
    :param app: pytest fixture
    :return: None
    """
    repo = BloodRequestRepository()
    assert len(repo.find_all()) == 100
    added_request = repo.find_one(1)
    assert added_request is not None
    repo.add(added_request)
    assert len(repo.find_all()) == 100
    b = BloodRequest(blood_req_id=1241, blood_group_id=2, location="asf", description="Asda", user_id=4)
    repo.add(b)
    assert len(repo.find_all()) == 101
    assert repo.find_one(1245) is None


def test_blood_request_repo_delete(app):
    """
    Function to test blood_request repository delete
    :param app: pytest fixture
    :return: None
    """
    repo = BloodRequestRepository()
    b = BloodRequest(blood_req_id=1241, blood_group_id=2, location="asf", description="Asda", user_id=4)
    repo.add(b)
    assert repo.delete(1241) is not None
    assert len(repo.find_all()) == 100
    assert repo.find_one(4) is not None
    assert repo.find_one(1241) is None


def test_blood_request_repo_update(app):
    """
    Function to test blood_request repository update
    :param app: pytest fixture
    :return: None
    """
    repo = BloodRequestRepository()
    b = BloodRequest(blood_req_id=1241, blood_group_id=2, location="asf", description="Asda", user_id=4)
    repo.add(b)

    b = BloodRequest(blood_req_id=1241, blood_group_id=5, location="asf", description="Asda", user_id=4)

    edit = repo.update(b)
    assert edit.blood_group_id == 5
    edit_user = repo.find_one(1241)
    assert edit_user.blood_group_id == 5
    b = BloodRequest(blood_req_id=1243, blood_group_id=2, location="asf", description="Asda", user_id=4)
    edit = repo.update(b)
    assert edit is None

