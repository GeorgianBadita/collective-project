from datetime import datetime, timedelta
import random
import string

from app.models.models import BloodGroup, User, Donation, BloodRequest


def generate_random_string(string_length=10):
    """
    Generate a random string of fixed length
    :param string_length: - length of the randomly generated string
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def generate_random_integer(lower, upper):
    """
    Function to generate random integer between lower and upper
    :param lower: lower limit of interval
    :param upper: upper limit of interval
    :return: random integer between [lower, upper]
    """
    return random.randint(lower, upper)


def populate_blood_group_table(db):
    """
    Function to populate the blood group table
    :param db: db context
    :return: None
    """
    names = ['0', 'A1', 'B2', 'AB']
    bl_group = [BloodGroup(name=names[i], rh=0) for i in range(4)]
    bl_group = bl_group + [BloodGroup(name=names[i], rh=1) for i in range(4)]
    for group in bl_group:
        db.session.add(group)
    db.session.commit()


def generate_random_users(count):
    """
    Function to generate random users
    :param count: number of users to be generated
    :return: list containing generated users
    """

    users = []

    for user_id in range(count):
        username = generate_random_string(10)
        email = '@'.join([generate_random_string(5), generate_random_string(5)]) + ".com"
        blood_group_id = generate_random_integer(1, 8)
        phone_number = str(generate_random_integer(1000000000, 9999999999))
        national_id = generate_random_string(13)
        last_donation_id = generate_random_integer(1, count)
        diseases = generate_random_string(5)
        about = generate_random_string(5)
        profile_pic = generate_random_string(5)
        if generate_random_integer(0, 1) == 1:
            profile_setup = True
        else:
            profile_setup = False

        users.append(User(user_id=str(user_id), username=username, email=email, phone_number=phone_number,
                          blood_group_id=blood_group_id, national_id=national_id, last_donation_id=last_donation_id,
                          diseases=diseases, about=about, profile_pic=profile_pic, profile_setup=profile_setup))
    return users


def generate_random_donations(count):
    """
    Function to generate random donations
    :param count: number of donations to be generated
    :return: list containing generated donatison
    """
    donations = []
    for _ in range(count):
        donor_id = generate_random_integer(1, count)
        date = datetime.now() + timedelta(days=generate_random_integer(0, count))
        if generate_random_integer(0, 1) == 1:
            request_id = generate_random_integer(1, count)
            donations.append(Donation(donor_id=donor_id, date=date, request_id=request_id))
        else:
            donations.append(Donation(donor_id=donor_id, date=date))
    return donations


def generate_random_blood_requests(count):
    """
    Function to generate random blood requests
    :param count: number of blood requests to be generated
    :return: list containing blood requests
    """
    blood_reqs = []
    for _ in range(count):
        blood_group_id = generate_random_integer(1, 8)
        location = generate_random_string(10)
        person_name = generate_random_string(10)
        description = generate_random_string(10)
        user_id = str(generate_random_integer(0, count - 1))
        blood_reqs.append(BloodRequest(blood_group_id=blood_group_id, location=location, description=description,
                                       person_name=person_name, user_id=user_id))

    return blood_reqs


def parse_date(dt):
    """
    Function to parse a given datetime
    :param dt: datetime string, with format (DD-MM-YYYY HH:MM:SS)
    :return:
    """
    splt = dt.split(" ")
    date = splt[0].split("-")
    time = splt[1].split(":")
    return datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))
