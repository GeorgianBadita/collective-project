from datetime import datetime, timedelta

from flask import json
from app.http.api import bp_api
from flask import request
from app.utils.utils import parse_date
from app.models.models import BloodRequest, Donation, User
from app.repository import userRepository, bloodRequestRepository, donationRepository


def json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}


@bp_api.route('/home', methods=['GET'])
def home():
    """
    View function which returns all blood requests
    :return: blood requests as json response
    """
    blood_requests = bloodRequestRepository.find_all()
    requests_response = {}
    for blood_request in blood_requests:
        requests_response[blood_request.blood_req_id] = blood_request.to_map()

    return json_response(requests_response)


@bp_api.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    View function to get a user's details
    :param user_id: id of the user
    :return: user's details if the users exists,
    error message and 404 status code otherwise
    """
    user = userRepository.find_one(user_id)
    if user is None:
        return json_response({"error_message": "User not found"}, status=404)
    return json_response({user.user_id: user.to_map()})


@bp_api.route('/blood_requests', methods=['POST'])
def add_blood_request():
    """
    Function to add a new blood_request from a form
    :return: The newly added blood_request if it is consistent,
    error messages and 400 or 404 status code messages otherwise
    """
    try:
        blood_req_id = request.form['blood_req_id']
        blood_group_id = request.form['blood_group_id']
        location = request.form['location']
        person_name = request.form['person_name']
        description = request.form['description']
        user_id = request.form['user_id']
    except KeyError as ex:
        return json_response({"error_message": "Missing fields"}, status=400)

    try:
        blood_req_id = int(blood_req_id)
        blood_group_id = int(blood_group_id)
    except ValueError as ex:
        return json_response({"error_message": "Invalid ids"}, status=400)
    if bloodRequestRepository.find_one(blood_req_id):
        return json_response({"error_message": "Blood request already exist!"}, status=400)
    if userRepository.find_one(user_id) is None:
        return json_response({"error_message": "User not found!"}, status=404)
    if blood_group_id not in range(9):
        return json_response({"error_message": "Invalid blood group!"}, status=400)
    new_blood_request = BloodRequest(blood_group_id=blood_group_id, location=location,
                                     person_name=person_name, description=description,
                                     user_id=user_id)
    bloodRequestRepository.add(new_blood_request)
    return json_response(new_blood_request.to_map(), status=200)


@bp_api.route("/donations", methods=['POST'])
def add_donation():
    """
    Function to add a new donation from a form
    :return: the newly added donation if it is consistent,
    error messages and 400, 404 status codes otherwise
    """
    try:
        donation_id = request.form['donation_id']
        donor_id = request.form['donor_id']
        date = request.form['date']
        request_id = request.form['request_id']
    except KeyError as ex:
        return json_response({"error_message": "Missing fields"}, status=400)

    try:
        donation_id = int(donation_id)
        donor_id = int(donor_id)
        if request_id is not "":
            request_id = int(request_id)
    except ValueError as ex:
        return json_response({"error_message": "Invalid ids"}, status=400)
    date = parse_date(date)
    print(date)
    if donationRepository.find_one(donation_id) is not None:
        return json_response({"error_message": "Donation already exist!"}, status=400)
    if userRepository.find_one(donor_id) is None:
        return json_response({"error_message": "User not found!"}, status=404)
    new_donation = Donation(donor_id=donor_id, date=date, request_id=request_id)
    donationRepository.add(new_donation)
    return json_response(new_donation.to_map(), status=200)


"""
    phone_number = db.Column(db.String(20))
    blood_group_id = db.Column(db.Integer, db.ForeignKey('blood_group.blood_group_id', use_alter=True), default=0)
    national_id = db.Column(db.String(20))
    last_donation_id = db.Column(db.Integer, db.ForeignKey('donation.donation_id', use_alter=True), nullable=True)
    diseases = db.Column(db.String(1024))
    about = db.Column(db.String(1024))
"""


@bp_api.route("/users/profile/<user_id>", methods=['PUT'])
def update_profile(user_id):
    """
    Function to update a user's profile
    :param user_id: id of the user who updates its profile
    :return: The updated user's profile if everything is ok,
    error messages and 400 or 404 status code otherwise
    """
    # TODO: verify that the current user is editing ts own profile
    try:
        phone_number = request.form['phone_number']
        blood_group_id = request.form['blood_group_id']
        national_id = request.form['national_id']
        last_donation_id = request.form['last_donation_id']
        diseases = request.form['diseases']
        about = request.form['about']
    except KeyError:
        return json_response({"error_message": "Missing fields!"}, status=400)
    try:
        blood_group_id = int(blood_group_id)
        last_donation_id = int(last_donation_id)
    except ValueError:
        return json_response({"error_message": "Invalid ids!"}, status=400)
    last_donation = donationRepository.find_one(last_donation_id)
    if last_donation is None:
        return json_response({"error_message": "Donation not found!"}, status=404)

    user = userRepository.find_one(user_id)
    if user is None:
        return json_response({"error_message": "User not found!"}, status=404)
    new_user = User(user_id=user_id, username=user.username, email=user.email, phone_number=phone_number,
                    blood_group_id=blood_group_id, national_id=national_id, last_donation_id=last_donation_id,
                    diseases=diseases, about=about, profile_setup=True, profile_pic=user.profile_pic)
    userRepository.update(new_user)
    return json_response(new_user.to_map())


@bp_api.route("/donations/accept/<donation_id>", methods=['PUT'])
def accept_donation(donation_id):
    """
    View function to accept a donation
    :param donation_id: id of the donation to be accepted
    :return: the accepted donation if everything works fine
    error message and 400 or 404 status codes
    """
    # TODO check that the user is involved in donation
    try:
        donation_id = int(donation_id)
    except ValueError:
        return json_response({"error_message": "Invalid ids!"}, status=400)
    donation = donationRepository.find_one(donation_id)
    if donation is None:
        return json_response({"error_message": "Donation not found!"})
    blood_request_id = donation.request_id
    if blood_request_id is not None:
        blood_request = bloodRequestRepository.find_one(donation.request_id)
        if blood_request is None:
            return json_response({"error_message": "Blood request not found!"})
        request_owner_id = blood_request.user_id
        # TODO check that the owner_id == current_user_id

    accepted_donation = Donation(donation_id=donation_id,
                                 date=datetime.now() + timedelta(hours=1),
                                 donor_id=donation.donor_id,
                                 request_id=donation.request_id,
                                 accepted=True)

    donationRepository.update(accepted_donation)
    return json_response(accepted_donation.to_map())