from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('route.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    email_re = request.form.get('emailre')
    username = request.form.get('username')
    password = request.form.get('password')
    password_re = request.form.get('passwordre')

    u = User.query.filter_by(email=email).first()

    # if the signup form is not well completed
    if u or email_re != email or password_re != password:
        if u:
            flash('Email address already in use!')
        if email != email_re:
            flash("Emails don't match!")
        if password != password_re:
            flash("Passwords don't match!")
        return redirect(url_for('auth.signup'))

    # create new user
    new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))

    # add the new user
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'
