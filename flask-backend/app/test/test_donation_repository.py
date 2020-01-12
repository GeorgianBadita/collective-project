from app.models.models import Donation
from app.repository import DonationRepository
from datetime import datetime, timedelta
from app.test.test_utils import app


def test_donation_repo_add_find_one_find_all(app):
    """
    Function to test donation repository add, find_one, find_all
    :param app: pytest fixture
    :return: None
    """
    repo = DonationRepository()
    assert len(repo.find_all()) == 100
    added_donation = repo.find_one(1)
    assert added_donation is not None
    repo.add(added_donation)
    assert len(repo.find_all()) == 100
    d = Donation(donation_id=5124, donor_id=1, date=datetime.now() + timedelta(days=1), request_id=5)
    repo.add(d)
    assert len(repo.find_all()) == 101
    assert repo.find_one(1245) is None


def test_donation_repo_delete(app):
    """
    Function to test donation repository delete
    :param app: pytest fixture
    :return: None
    """
    repo = DonationRepository()
    d = Donation(donation_id=5124, donor_id=1, date=datetime.now() + timedelta(days=1), request_id=5)
    repo.add(d)
    assert repo.delete(1) is not None
    assert len(repo.find_all()) == 100
    assert repo.find_one(4) is not None
    assert repo.find_one(1) is None


def test_donation_update(app):
    """
    Function to test donation repository update
    :param app: pytest fixture
    :return: None
    """
    repo = DonationRepository()
    d = Donation(donation_id=5124, donor_id=1, date=datetime.now() + timedelta(days=1), request_id=5)
    repo.add(d)

    d = Donation(donation_id=5124, donor_id=2, date=datetime.now() + timedelta(days=1), request_id=5)

    edit = repo.update(d)
    assert edit.donor_id == 2
    edit_user = repo.find_one(5124)
    assert edit_user.donor_id == 2
    d = Donation(donation_id=5555555555, donor_id=1, date=datetime.now() + timedelta(days=1), request_id=5)
    edit = repo.update(d)
    assert edit is None
