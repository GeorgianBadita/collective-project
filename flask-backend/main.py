
import os

# Third-party libraries
from flask import Flask
from flask_login import current_user
from oauthlib.oauth2 import WebApplicationClient
import requests

from app import create_app

app = create_app()

@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


if __name__ == "__main__":
    app.run(ssl_context="adhoc")