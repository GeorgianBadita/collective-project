from app import User
from app.repository import UserRepository
from app.test.test_utils import app

def test_user_repo_add_find_one_find_all(app):
    repo = UserRepository()
    assert len(repo.find_all()) == 101
    added_user = repo.find_one('18241211ajfh')
    assert added_user is not None
    repo.add(added_user)
    assert len(repo.find_all()) == 101
    u = User(user_id='18241211ajfh1', username='gabiis', email='gabiai@g.com', phone_number='+40 0752823713',
             blood_group_id=2, national_id='19907123512', diseases='asd', about='das', profile_pic='1',
             profile_setup=True)
    repo.add(u)
    assert len(repo.find_all()) == 102
    assert repo.find_one("asd") is None


def test_user_repo_delete(app):
    repo = UserRepository()
    u = User(user_id='18241211ajfh1', username='gabiis', email='gabiai@g.com', phone_number='+40 0752823713',
             blood_group_id=2, national_id='19907123512', diseases='asd', about='das', profile_pic='1',
             profile_setup=True)
    repo.add(u)
    assert repo.delete('18241211ajfh1') is not None
    assert len(repo.find_all()) == 101
    assert repo.find_one('18241211ajfh') is not None


def test_user_update(app):
    repo = UserRepository()
    u = User(user_id='18241211ajfh1', username='gabiis', email='gabiai@g.com', phone_number='+40 0752823713',
             blood_group_id=2, national_id='19907123512', diseases='asd', about='das', profile_pic='1',
             profile_setup=True)
    repo.add(u)

    u = User(user_id='18241211ajfh1', username='gabiis', email='gabiai@g.com', phone_number='+40 0752823713',
             blood_group_id=3, national_id='19907123512', diseases='asd', about='das', profile_pic='1',
             profile_setup=True)
    edit = repo.update(u)
    assert edit.blood_group_id == 3
    edit_user = repo.find_one('18241211ajfh1')
    assert edit_user.blood_group_id == 3
    u = User(user_id='x', username='gabiis', email='gabiai@g.com', phone_number='+40 0752823713',
             blood_group_id=3, national_id='19907123512', diseases='asd', about='das', profile_pic='1',
             profile_setup=True)
    edit = repo.update(u)
    assert edit is None
